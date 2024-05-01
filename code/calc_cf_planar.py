import os
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import torch
from pytomography.io.SPECT import simind
from pytomography.transforms.SPECT.attenuation import SPECTAttenuationTransform
from pytomography.transforms.SPECT.psf import SPECTPSFTransform
from pytomography.projectors.SPECT import SPECTSystemMatrix
from pytomography.algorithms import OSEM
from pytomography.likelihoods import PoissonLogLikelihood
from scipy.ndimage import gaussian_filter
import sim_method as sim

colors = np.loadtxt(r"C:\simind\mew20_3\pet_colors.txt").reshape(-1,3)/255.0
custom_cmap = LinearSegmentedColormap.from_list('custom_colormap', colors)

"""mainウィンドウのみ(b01)を使用して線量測定を行う"""
"""mew10%_3%"""
"""all interaction"""
photopeak_dir = r"C:\simind\mew20_3\calib\static_calib\l_main_cali.b01"
photopeak_hdr = r"C:\simind\mew20_3\calib\static_calib\l_main_cali.h00"
lower_dir = r"C:\simind\mew20_3\calib\static_calib\l_low_cali.b01"
lower_hdr = r"C:\simind\mew20_3\calib\static_calib\l_low_cali.h00"
upper_dir = r"C:\simind\mew20_3\calib\static_calib\l_up_cali.b01"
upper_hdr = r"C:\simind\mew20_3\calib\static_calib\l_up_cali.h00"
"""primary"""
# photopeak_dir = r"C:\simind\mew20_3\calib\static_calib\l_main_cali.b02"
# photopeak_hdr = r"C:\simind\mew20_3\calib\static_calib\l_main_cali.h00"
# lower_dir = r"C:\simind\mew20_3\calib\static_calib\l_low_cali.b02"
# lower_hdr = r"C:\simind\mew20_3\calib\static_calib\l_low_cali.h00"
# upper_dir = r"C:\simind\mew20_3\calib\static_calib\l_up_cali.b02"
# upper_hdr = r"C:\simind\mew20_3\calib\static_calib\l_up_cali.h00"

"""mew±10_10"""
# photopeak_dir = r"C:\simind\mew20_10\cali\static\mew20_10__main_cali_pl.b01"
# photopeak_hdr = r"C:\simind\mew20_10\cali\static\mew20_10__main_cali_pl.h00"
# lower_dir = r"C:\simind\mew20_10\cali\static\mew20_10__low_cali_pl.b01"
# lower_hdr = r"C:\simind\mew20_10\cali\static\mew20_10__low_cali_pl.h00"
# upper_dir = r"C:\simind\mew20_10\cali\static\mew20_10__up_cali_pl.b01"
# upper_hdr = r"C:\simind\mew20_10\cali\static\mew20_10__up_cali_pl.h00"
# """primary"""
# photopeak_dir = r"C:\simind\mew20_10\cali\static\mew20_10__main_cali_pl.b02"
# photopeak_hdr = r"C:\simind\mew20_10\cali\static\mew20_10__main_cali_pl.h00"
# lower_dir = r"C:\simind\mew20_10\cali\static\mew20_10__low_cali_pl.b02"
# lower_hdr = r"C:\simind\mew20_10\cali\static\mew20_10__low_cali_pl.h00"
# upper_dir = r"C:\simind\mew20_10\cali\static\mew20_10__up_cali_pl.b02"
# upper_hdr = r"C:\simind\mew20_10\cali\static\mew20_10__up_cali_pl.h00"

"""MEW15%_15%"""
# photopeak_dir = r"C:\simind\mew15\projections\cali_pl\mew15_main_cali_pl.b01"
# photopeak_hdr = r"C:\simind\mew15\projections\cali_pl\mew15_main_cali_pl.h00"
# lower_dir = r"C:\simind\mew15\projections\cali_pl\mew15_low_cali_pl.b01"
# lower_hdr = r"C:\simind\mew15\projections\cali_pl\mew15_low_cali_pl.h00"
# upper_dir = r"C:\simind\mew15\projections\cali_pl\mew15_up_cali_pl.b01"
# upper_hdr = r"C:\simind\mew15\projections\cali_pl\mew15_up_cali_pl.h00"
"""primary"""
# photopeak_dir = r"C:\simind\mew15\projections\cali_pl\mew15_main_cali_pl.b02"
# photopeak_hdr = r"C:\simind\mew15\projections\cali_pl\mew15_main_cali_pl.h00"
# lower_dir = r"C:\simind\mew15\projections\cali_pl\mew15_low_cali_pl.b02"
# lower_hdr = r"C:\simind\mew15\projections\cali_pl\mew15_low_cali_pl.h00"
# upper_dir = r"C:\simind\mew15\projections\cali_pl\mew15_up_cali_pl.b02"
# upper_hdr = r"C:\simind\mew15\projections\cali_pl\mew15_up_cali_pl.h00"

"""MEW15%_5%"""
# photopeak_dir = r"C:\simind\mew15_5\calib\static\mew15_5_main_cali_pl.b01"
# photopeak_hdr = r"C:\simind\mew15_5\calib\static\mew15_5_main_cali_pl.h00"
# lower_dir = r"C:\simind\mew15_5\calib\static\mew15_5_low_cali_pl.b01"
# lower_hdr = r"C:\simind\mew15_5\calib\static\mew15_5_low_cali_pl.h00"
# upper_dir = r"C:\simind\mew15_5\calib\static\mew15_5_up_cali_pl.b01"
# upper_hdr = r"C:\simind\mew15_5\calib\static\mew15_5_up_cali_pl.h00"

"""primary"""
# photopeak_dir = r"C:\simind\mew15_5\calib\static\mew15_5_main_cali_pl.b02"
# photopeak_hdr = r"C:\simind\mew15_5\calib\static\mew15_5_main_cali_pl.h00"
# lower_dir = r"C:\simind\mew15_5\calib\static\mew15_5_low_cali_pl.b02"
# lower_hdr = r"C:\simind\mew15_5\calib\static\mew15_5_low_cali_pl.h00"
# upper_dir = r"C:\simind\mew15_5\calib\static\mew15_5_up_cali_pl.b02"
# upper_hdr = r"C:\simind\mew15_5\calib\static\mew15_5_up_cali_pl.h00"

"""MEW10.5%_7%"""
# photopeak_dir = r"C:\simind\mew21_7\calib\static\mew21_main_cali_pl.b01"
# photopeak_hdr = r"C:\simind\mew21_7\calib\static\mew21_main_cali_pl.h00"
# lower_dir = r"C:\simind\mew21_7\calib\static\mew21_low_cali_pl.b01"
# lower_hdr = r"C:\simind\mew21_7\calib\static\mew21_low_cali_pl.h00"
# upper_dir = r"C:\simind\mew21_7\calib\static\mew21_up_cali_pl.b01"
# upper_hdr = r"C:\simind\mew21_7\calib\static\mew21_up_cali_pl.h00"
# CPS_per_MBq = 113.9559

dT = 30
activity = 50
cps_per_mbq = 0
repeat = 100

#.h00ファイルのname of data fileを変換する
sim.change_header_file_data(photopeak_hdr, photopeak_dir)
sim.change_header_file_data(lower_hdr, lower_dir)
sim.change_header_file_data(upper_hdr, upper_dir)

projections = simind.get_projections(photopeak_hdr)

s_TEW = simind.get_scatter_from_TEW(
    headerfile_lower=lower_hdr,
    headerfile_peak=photopeak_hdr,
    headerfile_upper=upper_hdr
)
object_meta, proj_meta = simind.get_metadata(photopeak_hdr)


for i in range(repeat):

    projections_noise = torch.poisson(projections*activity*dT)
    # calibration_factor = projections_noise
    s_TEW_noise = torch.poisson(s_TEW*activity*dT)
    calibration_factor = (projections_noise - s_TEW_noise) 
    calibration_factor[calibration_factor < 0] = 0
    pixel_size = object_meta.dx

    center_x, center_y, center_z = calibration_factor.shape[1] // 2, calibration_factor.shape[2] // 2, calibration_factor.shape[3] // 2
    radius = 3 / pixel_size

    calibration_factor = calibration_factor.cpu().numpy()

    total_sum_within_radius = np.sum(calibration_factor[
        0,
        max(center_x - int(radius), 0): min(center_x + int(radius) + 1, calibration_factor.shape[1]),
        max(center_y - int(radius), 0): min(center_y + int(radius) + 1, calibration_factor.shape[2]),
        max(center_z - int(radius), 0): min(center_z + int(radius) + 1, calibration_factor.shape[3])])
    
    cps_per_mbq += total_sum_within_radius/repeat/activity/dT
print(f"{cps_per_mbq}")

# Save the projections data as binary data
projections_file_path = r"C:\simind\mew15_5\calib\static\sc2.bin"
# GPU上のTensorをCPUに移動
# projections_cpu = s_TEW_noise.cpu()

# # TensorをNumPy配列に変換
# projections_np = projections_cpu.numpy()

# NumPy配列をバイナリファイルとして保存
# with open(projections_file_path, 'wb') as file:
    # calibration_factor.tofile(file)
# system_matrix = SPECTSystemMatrix(
#     obj2obj_transforms=[att_transform, psf_transform],
#     proj2proj_transforms=[],
#     object_meta=object_meta,
#     proj_meta=proj_meta
# )

# likelihood = PoissonLogLikelihood(system_matrix, projections_noise, additive_term=s_TEW)

# osem = OSEM(likelihood)
# # osem = OSEM(projections=projections_noise,
# #             system_matrix=system_matrix,
# #             scatter=s_TEW)

# source_prediction = osem(n_iters=10, n_subsets=8)
# print(source_prediction.shape)
# source_prediction = source_prediction[0].cpu().numpy()

# print(object_meta.dr)

# # ボクセルサイズを取得
# dr = np.prod(object_meta.dr)
# print(dr)
# # キャリブレーションファクター
# calibration_factor = 1 / CPS_per_MBq / dT / dr

# # count -> MBq / mL 
# source_prediction_MBpmL = source_prediction * calibration_factor

# print(f'{activity}___{source_prediction_MBpmL.sum() * dr}')

# # 3D Gaussian filter with FWHM=10mm to source_prediction_MBpmL
# source_prediction_MBpmL_gaussian = gaussian_filter(source_prediction_MBpmL, sigma=(2.355, 2.355, 2.355))




# roi_map, flg = sim.create_roi_map(r"C:\simind\symbia.inp", 'roi.bin', 128, 128, 128, 3.2957)
# roi_dicts = {}
# roi_map = roi_map.astype(np.float32)

# for f in range(1,flg+1, 1):
#     roi = np.where(roi_map == f, 1, 0)
    
#     calc = roi * source_prediction_MBpmL
#     num_elements = np.count_nonzero(calc > 0)
#     calc_sum = np.sum(calc)

#     roi_dicts[f] = [num_elements*dr, calc_sum*dr, calc_sum / num_elements]


# print(roi_dicts)


# plt.pcolormesh(roi_map[:,:,64].T, cmap='Greys_r')
# plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap=custom_cmap, alpha=0.5)
# # plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap='Greys_r')
# plt.colorbar(label='MBq/mL')
# plt.axis('off')
# plt.show()