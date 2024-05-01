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

colors = np.loadtxt(r"C:\simind\LE_penetrate\pet_colors.txt").reshape(-1,3)/255.0
custom_cmap = LinearSegmentedColormap.from_list('custom_colormap', colors)

"""mainウィンドウのみ(b01)を使用して線量測定を行う"""

# photopeak_dir = r"C:\simind\LE_penetrate\l_main.b01"
# photopeak_hdr = r"C:\simind\LE_penetrate\l_main.h00"
# att_dir = r"C:\simind\LE_penetrate\l_main.hct"
# inp_dir = r"C:\simind\LE_penetrate\symbia.inp"
# CPS_per_MBq = 180.2658  #LE


photopeak_dir = r"C:\simind\ME_penetrate\m_main.b01"
photopeak_hdr = r"C:\simind\ME_penetrate\m_main.h00"
att_dir = r"C:\simind\ME_penetrate\m_main.hct"
inp_dir = r"C:\simind\ME_penetrate\symbia.inp"
CPS_per_MBq = 133.0009   #ME


dT = 30
activity = 50

#.h00ファイルのname of data fileを変換する
sim.change_header_file_data(photopeak_hdr, photopeak_dir)

projections = simind.get_projections(photopeak_hdr)

projections_noise = torch.poisson(projections * activity * dT)

attenuation_map = simind.get_attenuation_map(att_dir)

# plt.subplots(1,3,figsize=(10,3))  # Changed from (1,3) to (1,2)
# plt.subplot(131)  # Changed from 131 to 121
# plt.pcolormesh(projections[0,0].cpu().T, cmap='nipy_spectral')
# plt.colorbar()
# plt.axis('off')
# plt.subplot(132)  # Changed from 132 to 122
# plt.pcolormesh(projections_noise[0,0].cpu().T, cmap='nipy_spectral')
# plt.colorbar()
# plt.axis('off')
# plt.subplot(133)
# plt.pcolormesh(attenuation_map[0,:,:,64].cpu().T, cmap='Greys_r')
# plt.colorbar(label='$cm^{-1}$')
# plt.axis('off')
# plt.show()


att_transform = SPECTAttenuationTransform(attenuation_map)

psf_meta = simind.get_psfmeta_from_header(photopeak_hdr)
psf_transform = SPECTPSFTransform(psf_meta)

object_meta, proj_meta = simind.get_metadata(photopeak_hdr)

# system_matrix = SPECTSystemMatrix(
#     obj2obj_transforms=[att_transform, psf_transform],
#     proj2proj_transforms=[],
#     object_meta=object_meta,
#     proj_meta=proj_meta
# )
system_matrix = SPECTSystemMatrix(
    obj2obj_transforms=[att_transform, ],
    proj2proj_transforms=[],
    object_meta=object_meta,
    proj_meta=proj_meta
)
likelihood = PoissonLogLikelihood(system_matrix, projections_noise)

osem = OSEM(likelihood)

source_prediction = osem(n_iters=10, n_subsets=8)
print(source_prediction.shape)
source_prediction = source_prediction[0].cpu().numpy()

print(object_meta.dr)

# ボクセルサイズを取得
dr = np.prod(object_meta.dr)
print(dr)
# キャリブレーションファクター
calibration_factor = 1 / CPS_per_MBq / dT / dr

# count -> MBq / mL 
source_prediction_MBpmL = source_prediction * calibration_factor

print(f'{activity}___{source_prediction_MBpmL.sum() * dr}')



# 3D Gaussian filter with FWHM=10mm to source_prediction_MBpmL
source_prediction_MBpmL = gaussian_filter(source_prediction_MBpmL, sigma=(2.355, 2.355, 2.355))

# plt.pcolormesh(attenuation_map[0,:,:,64].cpu().T, cmap='Greys_r')
# plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap=custom_cmap, alpha=0.8)
plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap='Greys_r')
plt.colorbar(label='MBq/mL')
plt.axis('off')
plt.show()