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
# lower_dir = r"C:\simind\LE_penetrate\l_low.b01"
# lower_hdr = r"C:\simind\LE_penetrate\l_low.h00"
# upper_dir = r"C:\simind\LE_penetrate\l_up.b01"
# upper_hdr = r"C:\simind\LE_penetrate\l_up.h00"
# CPS_per_MBq = 85.74  #180.2658  


photopeak_dir = r"C:\simind\ME_penetrate\m_main.b01"
photopeak_hdr = r"C:\simind\ME_penetrate\m_main.h00"
att_dir = r"C:\simind\ME_penetrate\m_main.hct"
lower_dir = r"C:\simind\ME_penetrate\m_low.b01"
lower_hdr = r"C:\simind\ME_penetrate\m_low.h00"
upper_dir = r"C:\simind\ME_penetrate\m_up.b01"
upper_hdr = r"C:\simind\ME_penetrate\m_up.h00"
CPS_per_MBq = 113.9559

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
# osem = OSEM(projections=projections_noise,
#             system_matrix=system_matrix,
#             scatter=s_TEW)

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
source_prediction_MBpmL_gaussian = gaussian_filter(source_prediction_MBpmL, sigma=(2.355, 2.355, 2.355))




roi_map, flg = sim.create_roi_map(r"C:\simind\symbia.inp", 'roi.bin', 128, 128, 128, 3.2957)
roi_dicts = {}
roi_map = roi_map.astype(np.float32)

for f in range(1,flg+1, 1):
    roi = np.where(roi_map == f, 1, 0)
    
    calc = roi * source_prediction_MBpmL
    num_elements = np.count_nonzero(calc > 0)
    calc_sum = np.sum(calc)

    roi_dicts[f] = [num_elements*dr, calc_sum*dr, calc_sum / num_elements]


print(roi_dicts)


plt.pcolormesh(roi_map[:,:,64].T, cmap='Greys_r')
plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap=custom_cmap, alpha=0.5)
# plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap='Greys_r')
plt.colorbar(label='MBq/mL')
plt.axis('off')
plt.show()