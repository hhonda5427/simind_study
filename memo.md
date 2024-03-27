## 123Iによるdosimetryにおいてコリメータの違いが定量性に与える影響

LEHRとMEコリメータで比較  
空間分解能 LEHR > ME  
penetration LEHR < ME
___  
シミュレーションで作成したデータ  
- LEHR  
    - main  
    - upper  
    - lower  
    - calib  
- ME  
    - main  
    - upper  
    - lower  
    - calib  

各エネルギーウィンドウに対してpenetration routineを使用しtotal, primary, penetration, scatterなどのデータを取得  

*.b01 = all type of interactions.   
 ->　検出された光子すべて  
*.b02 = Geometrical collimated primary attenuated photons from the phantom.  
   -> ファントムから直接放出された光子で、コリメーションされた光子  
*.b03 = Penetration of a septa from primary attenuated photons from the phantom.  
 -> ファントムから直接放出され、コリメータの隔壁を貫通した光子  
*.b04 = Scatter from the collimator from primary attenuated photons from the phantom.  
 -> ファントムから直接放出され、コリメータで散乱した光子  
*.b05 = X-rays from the collimator from primary attenuated photons from the phantom.  
-> ファントムから直接放出された光子がコリメータでX線を放出したもの  
*.b06 = Geometrical collimated from scattered photons from the phantom.  
-> ファントムから放出された散乱線で、コリメーションされた光子  
*.b07 = Penetration of a septa from scattered photons from the phantom.  
-> ファントムから放出された散乱線で、コリメータの隔壁を貫通した光子  
*.b08 = Scatter from the collimator from scattered photons from the phantom.  
-> ファントムから放出された散乱線が、コリメータで散乱した光子  
*.b09 = X-rays from the collimator from scattered photons from the phantom.  
-> ファントムから放出された散乱線がコリメータでX線を放出したもの  

結晶の後ろからの後方散乱がある場合の光子の挙動

*.b10 = Geometrical collimated primary attenuated photons from the phantom.  
   -> ファントムから直接放出された光子で、コリメーションされた光子  
*.b11 = Penetration of a septa from primary attenuated photons from the phantom.  
 -> ファントムから直接放出され、コリメータの隔壁を貫通した光子  
*.b12 = Scatter from the collimator from primary attenuated photons from the phantom.  
 -> ファントムから直接放出され、コリメータで散乱した光子  
*.b13 = X-rays from the collimator from primary attenuated photons from the phantom.  
-> ファントムから直接放出された光子がコリメータでX線を放出したもの  
*.b14 = Geometrical collimated from scattered photons from the phantom.  
-> ファントムから放出された散乱線で、コリメーションされた光子  
*.b15 = Penetration of a septa from scattered photons from the phantom.  
-> ファントムから放出された散乱線で、コリメータの隔壁を貫通した光子  
*.b16 = Scatter from the collimator from scattered photons from the phantom.  
-> ファントムから放出された散乱線が、コリメータで散乱した光子  
*.b17 = X-rays from the collimator from scattered photons from the phantom.  
-> ファントムから放出された散乱線がコリメータでX線を放出したもの  

*.b18 = photons without scattering and attenuation in the phantom  
-> ファントム内における散乱や減弱のない光子  
*.b19 = photons without scattering and attenuation in the phantom and geometrically collimated for primary photon energy  
-> ファントム内で散乱や減弱をしていない光子で、幾何学的にコリメーションされた光子  

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


