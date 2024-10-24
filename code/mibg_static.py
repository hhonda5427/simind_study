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
photopeak_dir = r"C:\simind\mibg_static_tot_w1.a00"
photopeak_hdr = r"C:\simind\mibg_static_tot_w1.h00"
# att_dir = r"C:\simind\mibg.hct"
# lower_dir = r"C:\simind\mibg_tot_w2.a00"
# lower_hdr = r"C:\simind\mibg_tot_w2.h00"
# upper_dir = r"C:\simind\mibg_tot_w3.a00"
# upper_hdr = r"C:\simind\mibg_tot_w3.h00"


dT = 30
activity = 110

#.h00ファイルのname of data fileを変換する
sim.change_header_file_data(photopeak_hdr, photopeak_dir)
projections = simind.get_projections(photopeak_hdr)


projections_noise = torch.poisson(projections * activity * dT)


# 軸を[depth, height, width]に変換
reshaped_projection = projections_noise[0].cpu().numpy()
# reshaped_prediction = source_prediction_gaussian.transpose((2, 1, 0))

# with open('mibg_ax_tot_ac.bin', 'wb') as f:
#     f.write(reshaped_prediction.tobytes())

with open('mibg_proj.bin','wb') as f:
    f.write(reshaped_projection.tobytes())

