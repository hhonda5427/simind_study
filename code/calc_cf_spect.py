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

# colors = np.loadtxt(r"C:\simind\LE_penetrate\pet_colors.txt").reshape(-1,3)/255.0
# custom_cmap = LinearSegmentedColormap.from_list('custom_colormap', colors)

"""mainウィンドウのみ(b01)を使用して線量測定を行う"""

"""mew10_3"""
# photopeak_dir = r"C:\simind\mew20_3\calib\spect_calib\l_main_cali_sp.b01"
# photopeak_hdr = r"C:\simind\mew20_3\calib\spect_calib\l_main_cali_sp.h00"
# lower_dir = r"C:\simind\mew20_3\calib\spect_calib\l_low_cali_sp.b01"
# lower_hdr = r"C:\simind\mew20_3\calib\spect_calib\l_low_cali_sp.h00"
# upper_dir = r"C:\simind\mew20_3\calib\spect_calib\l_up_cali_sp.b01"
# upper_hdr = r"C:\simind\mew20_3\calib\spect_calib\l_up_cali_sp.h00"

# photopeak_dir = r"C:\simind\mew20_3\calib\spect_calib\l_main_cali_sp.b02"
# photopeak_hdr = r"C:\simind\mew20_3\calib\spect_calib\l_main_cali_sp.h00"
# lower_dir = r"C:\simind\mew20_3\calib\spect_calib\l_low_cali_sp.b02"
# lower_hdr = r"C:\simind\mew20_3\calib\spect_calib\l_low_cali_sp.h00"
# upper_dir = r"C:\simind\mew20_3\calib\spect_calib\l_up_cali_sp.b02"
# upper_hdr = r"C:\simind\mew20_3\calib\spect_calib\l_up_cali_sp.h00"

"""mew10_10"""
# photopeak_dir = r"C:\simind\mew20_10\cali\spect\mew20_10__main_cali_sp.b01"
# photopeak_hdr = r"C:\simind\mew20_10\cali\spect\mew20_10__main_cali_sp.h00"
# lower_dir = r"C:\simind\mew20_10\cali\spect\mew20_10__low_cali_sp.b01"
# lower_hdr = r"C:\simind\mew20_10\cali\spect\mew20_10__low_cali_sp.h00"
# upper_dir = r"C:\simind\mew20_10\cali\spect\mew20_10__up_cali_sp.b01"
# upper_hdr = r"C:\simind\mew20_10\cali\spect\mew20_10__up_cali_sp.h00"

# photopeak_dir = r"C:\simind\mew20_10\cali\spect\mew20_10__main_cali_sp.b02"
# photopeak_hdr = r"C:\simind\mew20_10\cali\spect\mew20_10__main_cali_sp.h00"
# lower_dir = r"C:\simind\mew20_10\cali\spect\mew20_10__low_cali_sp.b02"
# lower_hdr = r"C:\simind\mew20_10\cali\spect\mew20_10__low_cali_sp.h00"
# upper_dir = r"C:\simind\mew20_10\cali\spect\mew20_10__up_cali_sp.b02"
# upper_hdr = r"C:\simind\mew20_10\cali\spect\mew20_10__up_cali_sp.h00"


"""mew15_15"""
# photopeak_dir = r"C:\simind\mew15\projections\cali_sp\mew15_main_cali_sp.b01"
# photopeak_hdr = r"C:\simind\mew15\projections\cali_sp\mew15_main_cali_sp.h00"
# lower_dir = r"C:\simind\mew15\projections\cali_sp\mew15_low_cali_sp.b01"
# lower_hdr = r"C:\simind\mew15\projections\cali_sp\mew15_low_cali_sp.h00"
# upper_dir = r"C:\simind\mew15\projections\cali_sp\mew15_up_cali_sp.b01"
# upper_hdr = r"C:\simind\mew15\projections\cali_sp\mew15_up_cali_sp.h00"

# photopeak_dir = r"C:\simind\mew15\projections\cali_sp\mew15_main_cali_sp.b02"
# photopeak_hdr = r"C:\simind\mew15\projections\cali_sp\mew15_main_cali_sp.h00"
# lower_dir = r"C:\simind\mew15\projections\cali_sp\mew15_low_cali_sp.b02"
# lower_hdr = r"C:\simind\mew15\projections\cali_sp\mew15_low_cali_sp.h00"
# upper_dir = r"C:\simind\mew15\projections\cali_sp\mew15_up_cali_sp.b02"
# upper_hdr = r"C:\simind\mew15\projections\cali_sp\mew15_up_cali_sp.h00"

"""mew15_5"""
photopeak_dir = r"C:\simind\mew15_5\calib\spect\mew15_5_main_cali_sp.b01"
photopeak_hdr = r"C:\simind\mew15_5\calib\spect\mew15_5_main_cali_sp.h00"
lower_dir = r"C:\simind\mew15_5\calib\spect\mew15_5_low_cali_sp.b01"
lower_hdr = r"C:\simind\mew15_5\calib\spect\mew15_5_low_cali_sp.h00"
upper_dir = r"C:\simind\mew15_5\calib\spect\mew15_5_up_cali_sp.b01"
upper_hdr = r"C:\simind\mew15_5\calib\spect\mew15_5_up_cali_sp.h00"

# photopeak_dir = r"C:\simind\mew15_5\calib\spect\mew15_5_main_cali_sp.b02"
# photopeak_hdr = r"C:\simind\mew15_5\calib\spect\mew15_5_main_cali_sp.h00"
# lower_dir = r"C:\simind\mew15_5\calib\spect\mew15_5_low_cali_sp.b02"
# lower_hdr = r"C:\simind\mew15_5\calib\spect\mew15_5_low_cali_sp.h00"
# upper_dir = r"C:\simind\mew15_5\calib\spect\mew15_5_up_cali_sp.b02"
# upper_hdr = r"C:\simind\mew15_5\calib\spect\mew15_5_up_cali_sp.h00"


"""MEW10.5_7"""
# photopeak_dir = r"C:\simind\mew21_7\calib\spect\mew21_main_cali_sp.b01"
# photopeak_hdr = r"C:\simind\mew21_7\calib\spect\mew21_main_cali_sp.h00"
# lower_dir = r"C:\simind\mew21_7\calib\spect\mew21_low_cali_sp.b01"
# lower_hdr = r"C:\simind\mew21_7\calib\spect\mew21_low_cali_sp.h00"
# upper_dir = r"C:\simind\mew21_7\calib\spect\mew21_up_cali_sp.b01"
# upper_hdr = r"C:\simind\mew21_7\calib\spect\mew21_up_cali_sp.h00"


dT = 30
activity = 50

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

projections_noise = torch.poisson(projections * activity * dT)
s_TEW = torch.poisson(s_TEW * activity * dT)

# attenuation_map = simind.get_attenuation_map(att_dir)

# att_transform = SPECTAttenuationTransform(attenuation_map)

psf_meta = simind.get_psfmeta_from_header(photopeak_hdr)
psf_transform = SPECTPSFTransform(psf_meta)

object_meta, proj_meta = simind.get_metadata(photopeak_hdr)

system_matrix = SPECTSystemMatrix(
    obj2obj_transforms=[psf_transform,],
    proj2proj_transforms=[],
    object_meta=object_meta,
    proj_meta=proj_meta
)

likelihood = PoissonLogLikelihood(system_matrix, projections_noise, additive_term=s_TEW)
# likelihood = PoissonLogLikelihood(system_matrix, projections)
osem = OSEM(likelihood)
# osem = OSEM(projections=projections_noise,
#             system_matrix=system_matrix,
#             scatter=s_TEW)

calibration_factor = osem(n_iters=10, n_subsets=8)

calibration_factor = calibration_factor[0].cpu().numpy()
calibration_factor[calibration_factor < 0] = 0
pixel_size = object_meta.dx

center_x, center_y, center_z = calibration_factor.shape[0] // 2, calibration_factor.shape[1] // 2, calibration_factor.shape[2] // 2
radius = 3 / pixel_size


total_sum_within_radius = np.sum(calibration_factor[
    max(center_x - int(radius), 0): min(center_x + int(radius) + 1, calibration_factor.shape[0]),
    max(center_y - int(radius), 0): min(center_y + int(radius) + 1, calibration_factor.shape[1]),
    max(center_z - int(radius), 0): min(center_z + int(radius) + 1, calibration_factor.shape[2])])
print(f"{calibration_factor.sum().item() / activity / dT},{total_sum_within_radius / activity / dT}")


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


# plt.pcolormesh(projections_noise[0,0,:,:].cpu().numpy(), cmap='Greys_r')
# # plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap=custom_cmap, alpha=0.5)
# # plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap='Greys_r')
# plt.colorbar(label='count/MBq')
# plt.axis('off')
# plt.show()