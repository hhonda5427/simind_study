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

colors = np.loadtxt(r'simind_study/pet_colors.txt').reshape(-1,3)/255.0
custom_cmap = LinearSegmentedColormap.from_list('custom_colormap', colors)

'''ペネトレーションルーチンで作成した各ファイルを読み込み、リスト化する'''
class SimindStudy:
    _header: dict
    _proj: dict[str, dict]

    def __init__(self, _dir: str) -> None:
        self._dir = _dir
        self._header = self.read_header_data(self._dir)
        self._proj = self.read_projection_data(self._dir, self._header)

    # 指定したディレクトリのファイルを読み込み、ファイル名とファイルの辞書を作成
    def read_header_data(self, input_dir: str) -> dict: 
        
        header_dict = {}
        files = os.listdir(input_dir)

        for file_name in files:
            file_path = os.path.join(input_dir, file_name)
            if os.path.isfile(file_path):
                _, extension = os.path.splitext(file_name)  #拡張子を取得
                
                if extension == '.h00':
                    header_dict['h00'] = file_path
                elif extension == '.hct':
                    header_dict['hct'] = file_path
                elif extension == '.ict':
                    header_dict['ict'] = file_path

        return header_dict

    # headerファイルの'imagefile' : 'name of data file'を任意のファイル名に書き換える
    def change_header_file_data(self, header_path: str, target_file_path: str):
        with open(header_path, 'r') as file:
            file_data = file.read()    
        file_data = re.sub(r'(?<=!name of data file := ).+', target_file_path.replace('\\', r'\\'), file_data)

        with open(header_path, 'w') as file:
            file.write(file_data)

    def read_projection_data(self, input_dir: str, header_dict: dict) -> dict:

        projections = {}
        files = os.listdir(input_dir)
        
        for file_name in files:
            file_path = os.path.join(input_dir, file_name)
            if os.path.isfile(file_path):
                _, extension = os.path.splitext(file_name)
                
                if re.match(r'\.b\d+$', extension):
                    data = {}
                    self.change_header_file_data(header_dict['h00'], file_path)
                    data['projections'] = simind.get_projections(header_dict['h00'])
                    data['attenuation_map'] = simind.get_attenuation_map(header_dict['hct'])
                    data['attenuation_transform'] = SPECTAttenuationTransform(data['attenuation_map'])
                    data['psf_meta'] = simind.get_psfmeta_from_header(header_dict['h00'])
                    data['psf_transform'] =SPECTPSFTransform(data['psf_meta'])
                    object_meta, proj_meta = simind.get_metadata(header_dict['h00'])
                    data['object_meta'] = object_meta
                    data['proj_meta'] = proj_meta

                    projections[file_name] = data

        return projections
    
    def osem_psf(self, n_iters:int, n_subsets:int, proj:torch.Tensor, data:dict, scatter=None) -> torch.Tensor:
        # att_transform = SPECTAttenuationTransform(data['attenuation_map'])
        # psf_transform = SPECTPSFTransform(data['psf_meta'])
        system_matrix = SPECTSystemMatrix(
            obj2obj_transforms=[data['attenuation_transform'], data['psf_transform']],
            proj2proj_transforms=[],
            object_meta=data['object_meta'],
            proj_meta=data['proj_meta']
        )
        likelihood = PoissonLogLikelihood(system_matrix, proj)

        osem = OSEM(likelihood)

        return osem(n_iters, n_subsets)
    
    @property
    def proj(self):
        return self._proj
    
main_dir = 'C:\\Users\\hhond\\source\\repos\\simind_study\\lehr_main'
upper_dir = 'C:\\Users\\hhond\\source\\repos\\simind_study\\lehr_up'
lower_dir = 'C:\\Users\\hhond\\source\\repos\\simind_study\\lehr_low'
calib_dir = 'C:\\Users\\hhond\\source\\repos\\simind_study\\lehr_cali'


lehr_main = SimindStudy(main_dir)
activity = 150
dT = 20

main = lehr_main.proj
b1 = main['lehr_main.b01']
b1_proj = b1['projections']
b1_att_map = b1['attenuation_map']
b1_proj_noise = torch.poisson(b1_proj * activity * dT)
b1_ax = lehr_main.osem_psf(6, 4, b1_proj_noise, b1, None)
b1_ax = b1_ax[0].cpu().numpy()
plt.pcolormesh(b1_att_map[0,:,:,128].cpu().T, cmap='Greys_r')
plt.pcolormesh(b1_ax[:,:,128].T, cmap=custom_cmap, alpha=0.8)
plt.colorbar(label='Counts')
plt.axis('off')
plt.show()