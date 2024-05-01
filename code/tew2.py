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

photopeak_dir = r"C:\simind\LE_scattwin\le_tot_w1.a00"
photopeak_hdr = r"C:\simind\LE_scattwin\le_tot_w1.h00"
att_dir = r"C:\simind\LE_scattwin\le.hct"
lower_dir = r"C:\simind\LE_scattwin\le_tot_w2.a00"
lower_hdr = r"C:\simind\LE_scattwin\le_tot_w2.h00"
upper_dir = r"C:\simind\LE_scattwin\le_tot_w3.a00"
upper_hdr = r"C:\simind\LE_scattwin\le_tot_w3.h00"
CPS_per_MBq = 95.3710


# photopeak_dir = r"C:\simind\ME_scattwin\me_tot_w1.a00"
# photopeak_hdr = r"C:\simind\ME_scattwin\me_tot_w1.h00"
# att_dir = r"C:\simind\ME_scattwin\me.hct"
# lower_dir = r"C:\simind\ME_scattwin\me_tot_w2.a00"
# lower_hdr = r"C:\simind\ME_scattwin\me_tot_w2.h00"
# upper_dir = r"C:\simind\ME_scattwin\me_tot_w3.a00"
# upper_hdr = r"C:\simind\ME_scattwin\me_tot_w3.h00"
# CPS_per_MBq = 133.1679 


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
s_TEW = torch.poisson(s_TEW*activity*dT)

attenuation_map = simind.get_attenuation_map(att_dir)

att_transform = SPECTAttenuationTransform(attenuation_map)

psf_meta = simind.get_psfmeta_from_header(photopeak_hdr)
psf_transform = SPECTPSFTransform(psf_meta)

object_meta, proj_meta = simind.get_metadata(photopeak_hdr)

system_matrix = SPECTSystemMatrix(
    obj2obj_transforms=[att_transform, psf_transform],
    proj2proj_transforms=[],
    object_meta=object_meta,
    proj_meta=proj_meta
)

likelihood = PoissonLogLikelihood(system_matrix, projections_noise, additive_term=s_TEW)

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