import os
import re
import numpy as np
from pytomography.io.SPECT import simind

# headerファイルの'imagefile' : 'name of data file'を任意のファイル名に書き換える
def change_header_file_data(header_path: str, target_file_path: str):
    with open(header_path, 'r') as file:
        file_data = file.read()    
    file_data = re.sub(r'(?<=!name of data file := ).+', target_file_path.replace('\\', r'\\'), file_data)

    with open(header_path, 'w') as file:
        file.write(file_data)

def create_roi_map(sphere_data_path, output_file_path, width, height, depth, voxel_size):
    # Initialize a 3D array with zeros
    array_3d = np.zeros((width, height, depth), dtype=np.float32)

    # Load the data from the synbia.inp file in the current directory
    with open(sphere_data_path, 'r') as f:
        spheres_data = [list(map(float, line.strip().split(","))) for line in f if line.strip()]
    
    # Convert the sphere data from cm to voxel units
    spheres_data = np.array(spheres_data) * 10  # 1 cm = 10 mm

    volume_center_x = width * voxel_size / 2
    volume_center_y = height * voxel_size / 2
    volume_center_z = depth * voxel_size / 2
    # Iterate over the spheres data
    flg = 0
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

    return array_3d, flg

# roi_map = create_roi_map("symbia.inp", 'inp.bin', 128, 128, 128, 4.4)
# import matplotlib.pyplot as plt
# plt.pcolormesh(roi_map[:,:,64].T, cmap='Greys_r', vmax=7)
# plt.colorbar(label='Counts')

def get_septa_penetrate_projections(photopeak:str, lower:str, upper:str):

    # Extract the file extension from photopeak_dir
    file_extension = os.path.splitext(photopeak)[1]
    # Change the file extension to '.b03'
    photopeak_dir = photopeak.replace(file_extension, '.b03')
    photopeak_hdr = photopeak.replace(file_extension, '.h00')
    lower_dir= lower.replace(file_extension, '.b03')
    lower_hdr = lower.replace(file_extension, '.h00')
    upper_dir= upper.replace(file_extension, '.b03')
    upper_hdr = upper.replace(file_extension, '.h00')    

    change_header_file_data(photopeak_hdr, photopeak_dir)
    change_header_file_data(lower_hdr, lower_dir)
    change_header_file_data(upper_hdr, upper_dir)    

    penetrate_projections = simind.get_projections(photopeak_hdr) 

    penetrate_TEW = simind.get_scatter_from_TEW(
        headerfile_lower=lower_hdr,
        headerfile_peak=photopeak_hdr,
        headerfile_upper=upper_hdr
    )
    projections = penetrate_projections - penetrate_TEW
    projections[projections < 0] = 0
    return projections

def get_septa_scatter_projections(photopeak:str, lower:str, upper:str):

    # Extract the file extension from photopeak_dir
    file_extension = os.path.splitext(photopeak)[1]
    # Change the file extension to '.b03'
    photopeak_dir = photopeak.replace(file_extension, '.b04')
    photopeak_hdr = photopeak.replace(file_extension, '.h00')
    lower_dir= lower.replace(file_extension, '.b04')
    lower_hdr = lower.replace(file_extension, '.h00')
    upper_dir= upper.replace(file_extension, '.b04')
    upper_hdr = upper.replace(file_extension, '.h00')    

    change_header_file_data(photopeak_hdr, photopeak_dir)
    change_header_file_data(lower_hdr, lower_dir)
    change_header_file_data(upper_hdr, upper_dir)    

    scatter_projections = simind.get_projections(photopeak_hdr) 

    scatter_TEW = simind.get_scatter_from_TEW(
        headerfile_lower=lower_hdr,
        headerfile_peak=photopeak_hdr,
        headerfile_upper=upper_hdr
    )
    projections = scatter_projections - scatter_TEW
    projections[projections < 0] = 0
    return projections

def get_primary_projections(photopeak:str):

    # Extract the file extension from photopeak_dir
    file_extension = os.path.splitext(photopeak)[1]
    # Change the file extension to '.b03'
    photopeak_dir = photopeak.replace(file_extension, '.b02')
    photopeak_hdr = photopeak.replace(file_extension, '.h00')

    change_header_file_data(photopeak_hdr, photopeak_dir)
    
    return simind.get_projections(photopeak_hdr)