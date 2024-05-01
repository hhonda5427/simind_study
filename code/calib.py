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

# photopeak_dir = r"C:\simind\LE_penetrate\calib\l_main_cali.b01"
# photopeak_hdr = r"C:\simind\LE_penetrate\calib\l_main_cali.h00"
# lower_dir = r"C:\simind\LE_penetrate\calib\l_low_cali.b01"
# lower_hdr = r"C:\simind\LE_penetrate\calib\l_low_cali.h00"
# upper_dir = r"C:\simind\LE_penetrate\calib\l_up_cali.b01"
# upper_hdr = r"C:\simind\LE_penetrate\calib\l_up_cali.h00"



photopeak_dir = r"C:\simind\ME_penetrate\calib\m_main_cali.b01"
photopeak_hdr = r"C:\simind\ME_penetrate\calib\m_main_cali.h00"
lower_dir = r"C:\simind\ME_penetrate\calib\m_low_cali.b01"
lower_hdr = r"C:\simind\ME_penetrate\calib\m_low_cali.h00"
upper_dir = r"C:\simind\ME_penetrate\calib\m_up_cali.b01"
upper_hdr = r"C:\simind\ME_penetrate\calib\m_up_cali.h00"


#.h00ファイルのname of data fileを変換する
sim.change_header_file_data(photopeak_hdr, photopeak_dir)
sim.change_header_file_data(lower_hdr, lower_dir)
sim.change_header_file_data(upper_hdr, upper_dir)

projections = simind.get_projections(photopeak_hdr)

g_above = simind.get_projections(upper_hdr)
g_below = simind.get_projections(lower_hdr)
w_above = w_below = 4.77
w_peak = 174.9 - 143.1

s_TEW = projections - (g_above/w_above + g_below/w_below)*w_peak / 2

s_TEW2 = simind.get_scatter_from_TEW(
    headerfile_lower=lower_hdr,
    headerfile_peak=photopeak_hdr,
    headerfile_upper=upper_hdr
)


print(s_TEW.shape)
print(projections.sum().item())
print(s_TEW.sum().item())
print(s_TEW2.sum().item())


plt.subplots(1,2,figsize=(7,3))
plt.subplot(121)
plt.pcolormesh(s_TEW[0,0,:,:].cpu().T, cmap=custom_cmap, alpha=0.8)
# plt.pcolormesh(source_prediction_MBpmL[:,:,64].T, cmap='Greys_r')
plt.colorbar(label='cps/MBq')
plt.axis('off')
plt.subplot(122)
plt.pcolormesh(s_TEW2[0,0,:,:].cpu().T, cmap=custom_cmap, alpha=0.8)
plt.colorbar(label='cps/MBq')
plt.axis('off')
plt.show()