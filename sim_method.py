import os
import re
import numpy as np

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
    flg = 1
    for sphere in spheres_data:
        # flg += 1
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