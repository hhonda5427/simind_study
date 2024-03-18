import numpy as np
import pytomography
from pytomography.io.SPECT import simind
from pytomography.transforms import SPECTAttenuationTransform, SPECTPSFTransform
from pytomography.projectors import SPECTSystemMatrix
from pytomography.algorithms import OSEM, FilteredBackProjection
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
import torch
import re

colors = np.loadtxt('pet_colors.txt').reshape(-1,3)/255.0
custom_cmap = LinearSegmentedColormap.from_list('custom_colormap', colors)


def change_header_name_of_data_file(file_path, new_file_name):
    with open(file_path, 'r') as file:
        file_data = file.read()
    
    file_data = re.sub(r'(?<=!name of data file := ).+', new_file_name, file_data)

    with open(file_path, 'w') as file:
        file.write(file_data)

# *.h00のデータを書き換えファイル名を変更する
def create_header_file(file_path, new_file_path, rewrite_data):
    with open(file_path, 'r') as file:
        file_data = file.read()

    file_data = re.sub(r'(?<=!name of data file := ).+', rewrite_data, file_data) 

    with open(new_file_path, 'w') as new_file:
        new_file.write(file_data)


def save_binary_file(data, file_path):
# Save the source_prediction as binary data
    with open(file_path, 'wb') as f:
        output = np.transpose(data, (2, 1, 0))  # Transpose to depth, height, width order
        f.write(output.tobytes())

def read_binary_file(file_path, width, height, depth):
    with open(file_path, 'rb') as f:
        data = np.frombuffer(f.read(), dtype=np.float32)
        data = data.reshape((width, height, depth))

    return np.transpose(data, (2, 1, 0))


def create_roi_map(sphere_file_path, output_file_path, width, height, depth, voxel_size):
    # Initialize a 3D array with zeros
    array_3d = np.zeros((width, height, depth), dtype=np.float32)

    # Load the data from the synbia.inp file in the current directory
    with open(sphere_file_path, 'r') as f:
        spheres_data = [list(map(float, line.strip().split(","))) for line in f if line.strip()]
    
    # Convert the sphere data from cm to voxel units
    spheres_data = np.array(spheres_data) * 10  # 1 cm = 10 mm

    volume_center_x = width * voxel_size / 2
    volume_center_y = height * voxel_size / 2
    volume_center_z = depth * voxel_size / 2
    # Iterate over the spheres data
    flg = 1
    for sphere in spheres_data:
        flg += 1
        radius_z, radius_x, radius_y, center_z, center_x, center_y, _, _ = sphere
        
        target_center_x = volume_center_x + center_x
        target_center_y = volume_center_y - center_y
        target_center_z = volume_center_z + center_z
        # Iterate over the 3D array
        for k in range(depth):
            for j in range(height):
                for i in range(width):
                    # Calculate the distance from the center of the sphere
                    dist_x = (i * voxel_size + voxel_size / 2 - target_center_x) ** 2 / radius_x ** 2
                    dist_y = (j * voxel_size + voxel_size / 2 - target_center_y) ** 2 / radius_y ** 2
                    dist_z = (k * voxel_size + voxel_size / 2 - target_center_z) ** 2 / radius_z ** 2
                    # If the voxel is inside the sphere, set its value to 1
                    if dist_x + dist_y + dist_z <= 1:
                        array_3d[i, j, k] = flg

    # Write the 3D array to a binary file
    with open(output_file_path, 'wb') as f:
        f.write(array_3d.astype(np.float32).tobytes())

    return array_3d

# roi_map = create_roi_map("symbia.inp", 'inp.bin', 128, 128, 128, 4.4)
# import matplotlib.pyplot as plt
# plt.pcolormesh(roi_map[:,:,64].T, cmap='Greys_r', vmax=7)
# plt.colorbar(label='Counts')


def reconstruction(target_file_path, header_file_path, attenuation_file_path):

    attenuation_map = simind.get_attenuation_map(attenuation_file_path)
    projections = simind.get_projections(header_file_path)
    att_transform = SPECTAttenuationTransform(attenuation_map)

    psf_meta = simind.get_psfmeta_from_header(header_file_path)
    psf_transform = SPECTPSFTransform(psf_meta)

    object_meta, proj_meta = simind.get_metadata(header_file_path)

    system_matrix = SPECTSystemMatrix(
        obj2obj_transforms=[att_transform, psf_transform],     #attenuation, psf
        proj2proj_transforms=[],
        object_meta=object_meta,
        proj_meta=proj_meta
    )
