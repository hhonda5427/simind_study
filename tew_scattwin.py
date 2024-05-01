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

total_w1_hdr = r'C:\Users\hhond\source\repos\simind_study\LE\le_tot_w1.h00'
total_w2_hdr = r'C:\Users\hhond\source\repos\simind_study\LE\le_tot_w2.h00'
total_w3_hdr = r'C:\Users\hhond\source\repos\simind_study\LE\le_tot_w3.h00'
scat_true_hdr = r'C:\Users\hhond\source\repos\simind_study\LE\le_sca_w1.h00'
att_hdr = r'C:\Users\hhond\source\repos\simind_study\LE\le.hct'


s_true = simind.get_projections(scat_true_hdr)
s_TEW = simind.get_scatter_from_TEW(
    headerfile_lower=total_w2_hdr,
    headerfile_upper=total_w3_hdr,
    headerfile_peak=total_w1_hdr
)

print(s_TEW.sum().item())
print(s_true.sum().item())


CPS_per_MBq = 95.3710
dT = 20
activity = 50

s_TEW_noise = torch.poisson(s_TEW*activity*dT)

attenuation_map = simind.get_attenuation_map(att_hdr)

att_transform = SPECTAttenuationTransform(attenuation_map)

psf_meta = simind.get_psfmeta_from_header(total_w1_hdr)
psf_transform = SPECTPSFTransform(psf_meta)

object_meta, proj_meta = simind.get_metadata(total_w1_hdr)

system_matrix = SPECTSystemMatrix(
    obj2obj_transforms=[att_transform, psf_transform],
    proj2proj_transforms=[],
    object_meta=object_meta,
    proj_meta=proj_meta
)

likelihood = PoissonLogLikelihood(system_matrix, s_TEW_noise, additive_term=s_TEW)

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