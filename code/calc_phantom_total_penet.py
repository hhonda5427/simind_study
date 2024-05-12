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

colors = np.loadtxt(r"C:\simind\pet_colors.txt").reshape(-1,3)/255.0
custom_cmap = LinearSegmentedColormap.from_list('custom_colormap', colors)

"""mew10_3"""
# photopeak_dir = r"C:\simind\mew20_3\l_main.b01"
# photopeak_hdr = r"C:\simind\mew20_3\l_main.h00"
# att_dir = r"C:\simind\mew20_3\l_main.hct"
# lower_dir = r"C:\simind\mew20_3\l_low.b01"
# lower_hdr = r"C:\simind\mew20_3\l_low.h00"
# upper_dir = r"C:\simind\mew20_3\l_up.b01"
# upper_hdr = r"C:\simind\mew20_3\l_up.h00"
# CPS_per_MBq = 67.9205 #spect with septa correction 67.9205

"""mew10_10"""
photopeak_dir = r"C:\simind\mew20_10\projections\mew20_10__main.b01"
photopeak_hdr = r"C:\simind\mew20_10\projections\mew20_10__main.h00"
att_dir = r"C:\simind\mew20_10\projections\mew20_10__main.hct"
lower_dir = r"C:\simind\mew20_10\projections\mew20_10__low.b01"
lower_hdr = r"C:\simind\mew20_10\projections\mew20_10__low.h00"
upper_dir = r"C:\simind\mew20_10\projections\mew20_10__up.b01"
upper_hdr = r"C:\simind\mew20_10\projections\mew20_10__up.h00"
CPS_per_MBq = 70.3114 #spect with septa correction 70.3114

"""MEW15"""
# photopeak_dir = r"C:\simind\mew15\projections\phantom\mew15_main.b01"
# photopeak_hdr = r"C:\simind\mew15\projections\phantom\mew15_main.h00"
# att_dir = r"C:\simind\mew15\projections\phantom\mew15_main.hct"
# lower_dir = r"C:\simind\mew15\projections\phantom\mew15_low.b01"
# lower_hdr = r"C:\simind\mew15\projections\phantom\mew15_low.h00"
# upper_dir = r"C:\simind\mew15\projections\phantom\mew15_up.b01"
# upper_hdr = r"C:\simind\mew15\projections\phantom\mew15_up.h00"
# CPS_per_MBq = 64.5912    #spect with septa correction 64.5912

"""MEW15%_5%"""
# photopeak_dir = r"C:\simind\mew15_5\projections\mew15_5_main.b01"
# photopeak_hdr = r"C:\simind\mew15_5\projections\mew15_5_main.h00"
# att_dir = r"C:\simind\mew15_5\projections\mew15_5_main.hct"
# lower_dir = r"C:\simind\mew15_5\projections\mew15_5_low.b01"
# lower_hdr = r"C:\simind\mew15_5\projections\mew15_5_low.h00"
# upper_dir = r"C:\simind\mew15_5\projections\mew15_5_up.b01"
# upper_hdr = r"C:\simind\mew15_5\projections\mew15_5_up.h00"
# CPS_per_MBq = 59.5251    #spect with septa correction 59.5251

"""MEW21_7"""
# photopeak_dir = r"C:\simind\mew21_7\mew21_main.b01"
# photopeak_hdr = r"C:\simind\mew21_7\mew21_main.h00"
# att_dir = r"C:\simind\mew21_7\mew21_main.hct"
# lower_dir = r"C:\simind\mew21_7\mew21_low.b01"
# lower_hdr = r"C:\simind\mew21_7\mew21_low.h00"
# upper_dir = r"C:\simind\mew21_7\mew21_up.b01"
# upper_hdr = r"C:\simind\mew21_7\mew21_up.h00"
# CPS_per_MBq = 82.4289    #static 82.36  #spect 82.4289

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
# s_TEW = torch.poisson(s_TEW*activity*dT)

attenuation_map = simind.get_attenuation_map(att_dir)

att_transform = SPECTAttenuationTransform(attenuation_map)

roi_map = attenuation_map[0].cpu().numpy()
roi_map = np.where(roi_map > 0 , 1, 0)


psf_meta = simind.get_psfmeta_from_header(photopeak_hdr)
psf_transform = SPECTPSFTransform(psf_meta)

object_meta, proj_meta = simind.get_metadata(photopeak_hdr)

system_matrix = SPECTSystemMatrix(
    obj2obj_transforms=[att_transform, psf_transform],
    proj2proj_transforms=[],
    object_meta=object_meta,
    proj_meta=proj_meta,
    n_parallel=2
)

"""septa process"""
penetrate_TEW = sim.get_septa_penetrate_projections(
    photopeak_dir,
    lower_dir,
    upper_dir
)


scatter_TEW = sim.get_septa_scatter_projections(
    photopeak_dir,
    lower_dir,
    upper_dir    
)

"""end septa process"""


corr_TEW = s_TEW + scatter_TEW + penetrate_TEW
corr_TEW = torch.poisson(corr_TEW * activity * dT)

# with scatter 
likelihood = PoissonLogLikelihood(
    system_matrix=system_matrix, 
    projections=projections_noise, 
    additive_term=corr_TEW
    )

# without scatter
# likelihood = PoissonLogLikelihood(
#     system_matrix=system_matrix, 
#     projections=projections_noise
#     )



osem = OSEM(likelihood)
source_prediction = osem(n_iters=10, n_subsets=8)
# print(source_prediction.shape)
source_prediction = source_prediction[0].cpu().numpy()

# print(object_meta.dr)

# ボクセルサイズを取得
dr = np.prod(object_meta.dr)
# print(dr)
# キャリブレーションファクター
calibration_factor = 1 / CPS_per_MBq / dT / dr

# count -> MBq / mL 
source_prediction_MBqpmL = source_prediction * calibration_factor

# 3D Gaussian filter with FWHM=8mm to source_prediction_MBpmL
# σ = (FWHM / pixel size) / ( 2 √(2 ln(2)))

source_prediction_MBqpmL_gaussian = gaussian_filter(source_prediction_MBqpmL, sigma=(1.885, 1.885, 1.885))


source_prediction_MBqpmL_within_roimap = source_prediction_MBqpmL * roi_map
# source_prediction_MBqpmL_within_roimap = source_prediction_MBqpmL_gaussian * roi_map
print(f'{activity}___{source_prediction_MBqpmL.sum() * dr}____{source_prediction_MBqpmL_within_roimap.sum()*dr}')






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
# plt.pcolormesh(source_prediction_MBqpmL[:,:,64].T, cmap='Greys')
# plt.pcolormesh(source_prediction_MBqpmL_gaussian[:,:,64].T, cmap='Greys')

# plt.colorbar(label='MBq/mL')
# plt.axis('off')
# plt.show()