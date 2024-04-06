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
import sim_method as sim

colors = np.loadtxt(r'pet_colors.txt').reshape(-1,3)/255.0
custom_cmap = LinearSegmentedColormap.from_list('custom_colormap', colors)

"""mainウィンドウのみ(b01)を使用して線量測定を行う"""

photopeak_dir = r'C:\Users\hhond\source\repos\simind_study\lehr_main_t\lehr_main_t.b01'
photopeak_hdr = r'C:\Users\hhond\source\repos\simind_study\lehr_main_t\lehr_main_t.h00'
att_dir = r'C:\Users\hhond\source\repos\simind_study\lehr_main_t\lehr_main_t.hct'

# ペネトレーションイベント
b03_dir = r'C:\Users\hhond\source\repos\simind_study\lehr_main_t\lehr_main_t.b03'
b07_dir = r'C:\Users\hhond\source\repos\simind_study\lehr_main_t\lehr_main_t.b07'
b11_dir = r'C:\Users\hhond\source\repos\simind_study\lehr_main_t\lehr_main_t.b11'
b15_dir = r'C:\Users\hhond\source\repos\simind_study\lehr_main_t\lehr_main_t.b15'

CPS_per_MBq = 109.0181

dT = 20
activity = 50

#.h00ファイルのname of data fileを変換する
sim.change_header_file_data(photopeak_hdr, photopeak_dir)
projections = simind.get_projections(photopeak_hdr)

sim.change_header_file_data(photopeak_hdr, b03_dir)
b03 = simind.get_projections(photopeak_hdr)

sim.change_header_file_data(photopeak_hdr, b07_dir)
b07 = simind.get_projections(photopeak_hdr)

sim.change_header_file_data(photopeak_hdr, b11_dir)
b11 = simind.get_projections(photopeak_hdr)

sim.change_header_file_data(photopeak_hdr, b15_dir)
b15 = simind.get_projections(photopeak_hdr)
penetrations = b03 + b07 + b11 + b15



no_penetrations = projections - penetrations
no_penetrations[no_penetrations < 0] = 0
# no_penetrations = torch.from_numpy(no_penetrations)

projections_noise = torch.poisson(no_penetrations * activity * dT)

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

likelihood = PoissonLogLikelihood(system_matrix, projections_noise)

osem = OSEM(likelihood)

source_prediction = osem(n_iters=6, n_subsets=4)
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


plt.pcolormesh(attenuation_map[0,:,:,64].cpu().T, cmap='Greys_r')
plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap=custom_cmap, alpha=0.8)
plt.colorbar(label='MBq/mL')
plt.axis('off')
plt.show()