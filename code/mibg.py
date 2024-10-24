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
photopeak_dir = r"C:\simind\i123_mibg_tot_w1.a00"
photopeak_hdr = r"C:\simind\i123_mibg_tot_w1.h00"
# photopeak_dir = r"C:\simind\i123_mibg_air_w1.a00"
# photopeak_hdr = r"C:\simind\i123_mibg_air_w1.h00"
att_dir = r"C:\simind\i123_mibg.hct"
lower_dir = r"C:\simind\i123_mibg_tot_w2.a00"
lower_hdr = r"C:\simind\i123_mibg_tot_w2.h00"
upper_dir = r"C:\simind\i123_mibg_tot_w3.a00"
upper_hdr = r"C:\simind\i123_mibg_tot_w3.h00"


dT = 19
activity = 100

#.h00ファイルのname of data fileを変換する
# sim.change_header_file_data(photopeak_hdr, photopeak_dir)
# sim.change_header_file_data(lower_hdr, lower_dir)
# sim.change_header_file_data(upper_hdr, upper_dir)

projections = simind.get_projections(photopeak_hdr)

s_TEW = simind.get_scatter_from_TEW(
    headerfile_lower=lower_hdr,
    headerfile_peak=photopeak_hdr,
    headerfile_upper=upper_hdr
)

projections_noise = torch.poisson(projections * activity * dT)
s_TEW = torch.poisson(s_TEW*activity*dT)

attenuation_map = simind.get_attenuation_map(att_dir)



att_transform = SPECTAttenuationTransform(attenuation_map)

psf_meta = simind.get_psfmeta_from_header(photopeak_hdr)
psf_transform = SPECTPSFTransform(psf_meta)

object_meta, proj_meta = simind.get_metadata(photopeak_hdr)

# system_matrix = SPECTSystemMatrix(
#     obj2obj_transforms=[ psf_transform],
#     proj2proj_transforms=[],
#     object_meta=object_meta,
#     proj_meta=proj_meta,
#     n_parallel=2
# )
system_matrix = SPECTSystemMatrix(
    obj2obj_transforms=[att_transform, psf_transform],
    proj2proj_transforms=[],
    object_meta=object_meta,
    proj_meta=proj_meta,
    n_parallel=2
)
# with scatter 
# likelihood = PoissonLogLikelihood(
#     system_matrix=system_matrix, 
#     projections=projections_noise, 
#     additive_term=s_TEW
#     )

# without scatter
likelihood = PoissonLogLikelihood(
    system_matrix=system_matrix, 
    projections=projections
    )



osem = OSEM(likelihood)
source_prediction = osem(n_iters=6, n_subsets=8)
# print(source_prediction.shape)
source_prediction = source_prediction[0].cpu().numpy()

# print(object_meta.dr)

# ボクセルサイズを取得
dr = np.prod(object_meta.dr)


# 3D Gaussian filter with FWHM=8mm to source_prediction_MBpmL
# σ = (FWHM / pixel size) / ( 2 √(2 ln(2)))
source_prediction_gaussian = gaussian_filter(source_prediction, sigma=(1,1,1))

# attenuation_map_cpu = attenuation_map[0].cpu().numpy()

# print(attenuation_map_cpu.shape)

# fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# axes[0].imshow(attenuation_map_cpu[:,:,64], cmap='gray')
# axes[0].set_title('Attenuation Map')
# # axes[0].colorbar()  # カラーバーを追加

# axes[1].imshow(source_prediction_gaussian[:,:,64], cmap='gray')
# axes[1].set_title('Source Prediction Gaussian')
# # axes[1].colorbar()  # カラーバーを追加

# plt.show()


# 軸を[depth, height, width]に変換
# reshaped_projection = projections_noise[0].cpu().numpy()
reshaped_prediction = source_prediction_gaussian.transpose((2, 1, 0))

with open('mibg_ax_full_ac.bin', 'wb') as f:
    f.write(reshaped_prediction.tobytes())

# with open('mibg_proj_air.bin','wb') as f:
#     f.write(reshaped_projection.tobytes())

# with open('mibg_air.bin', 'wb') as f:
#     f.write(source_prediction.transpose((2,1,0)).tobytes())


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