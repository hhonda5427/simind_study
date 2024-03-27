import os
import re
import numpy as np
import torch
from pytomography.io.SPECT import simind
from pytomography.transforms.SPECT.attenuation import SPECTAttenuationTransform
from pytomography.transforms.SPECT.psf import SPECTPSFTransform

'''ペネトレーションルーチンで作成した各ファイルを読み込み、リスト化する'''
class SimindStudy:
    main_header: dict
    upper_header: dict
    lower_header: dict
    calib_header: dict

    main_proj: dict[str, dict]       
    upper_proj: dict[str, dict]
    lower_proj: dict[str, dict]
    calib_proj: dict[str, dict]

    def __init__(self, main_dir: str, upper_dir: str, lower_dir: str, calib_dir: str) -> None:
        self.main_dir = main_dir
        self.upper_dir = upper_dir
        self.lower_dir = lower_dir
        self.calib_dir = calib_dir

        self.main_header = self.read_header_data(self.main_dir)
        self.upper_header = self.read_header_data(self.upper_dir)
        self.lower_header = self.read_header_data(self.lower_dir)
        self.calib_header = self.read_header_data(self.calib_dir)

        self.main_proj = self.read_projection_data(self.main_dir, self.main_header)
        self.upper_proj = self.read_projection_data(self.upper_dir, self.upper_header)
        self.lower_proj = self.read_projection_data(self.lower_dir, self.lower_header)
        self.calib_proj = self.read_projection_data(self.calib_dir, self.calib_header)
        
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
    
main_dir = 'C:\\Users\\hhond\\source\\repos\\simind_study\\lehr_main'
upper_dir = 'C:\\Users\\hhond\\source\\repos\\simind_study\\lehr_up'
lower_dir = 'C:\\Users\\hhond\\source\\repos\\simind_study\\lehr_low'
calib_dir = 'C:\\Users\\hhond\\source\\repos\\simind_study\\lehr_cali'

lehr_study = SimindStudy(main_dir, upper_dir, lower_dir, calib_dir)

activity = 150
dT = 20

main = lehr_study.main_proj

