## 123Iによるdosimetryにおいてコリメータの違いが定量性に与える影響

LEHRとMEコリメータで比較
空間分解能 LEHR > ME
penetration LEHR < ME

jaszakファントムを使用して比較


####  symbiaT16シミレーション環境の構築
##### シンチレーションカメラ  
___  
index19  
Photon direction = 3

___  
energy resulution index22    
- energy resolution  index22 = 0 あるいは switch /FE:filename 
- index98 = 1 として　FWHM = a + b√(Ene + cEne^2)  を設定する
- 設定方法は simind.iniの46,47,48でa,b,cを設定可能
- symbiaのエネルギー分解能はFWHM = -0.534 + 0.946√(E+0.006E^2)　として.erfファイルで設定する
___  
index24  
Number of photon Histrories * 1E6(試行回数)  =   100  
___  
index27  
keV/channel = 2.00  
___  
index28  
pixel size in simulated image  
ズーム変更時にもここでピクセルサイズを変更する  
___
##### コリメータパラメータ　　
___  
index53  
collimator routine = 1  
penetrationなどをシミュレーションするときには使用する  
___  
index59  
Random collimator movement = 1  
解析モデルでは表現できないスターアーチファクトをシミュレートする  
___  
index80  
Energy spectra channels = 512  
表現できるエネルギーの範囲は0～1024keVまで  
___  
index84  
Scoring routine = 4 penetrate  
___
index98  
Energy resolution model = 1  
エネルギー分解能ファイルを読み込む際はswitch /FE:filenameを使用する　　
___
### multiple sphere source  
Jaszcak cylindrical pahntom  


