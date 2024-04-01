## 123Iによるdosimetryにおいてコリメータの違いが定量性に与える影響
  
LEHRとMEコリメータで比較  
空間分解能 LEHR > ME  
penetration LEHR < ME
1. mainウィンドウのみの場合の定量精度
2. プライマリー光子のみの場合の定量精度  
3. TEW処理を行った場合の定量精度  
4. 上記の3つの定量精度をLEHRとMEコリメータで比較する。  
5. LEHRとMEコリメータでセプタを貫通を阻止する能力がどの程度あるか  
6. 被写体サイズにより貫通する光子がどの程度増加するか（可能であれば）  
___


### 収集条件（一般 LEHR or LMEGP）  
- 収集エネルギー　-> 159keV(20%)  
- マトリクスサイズ -> 128 * 128  
- 収集角度 -> 360度  
- 収集時間 -> 6時間 = 20～25s/step,  
&emsp; &emsp; &emsp; &emsp; &ensp; 24時間 = 30～40s/step  
- 収集ステップ数 -> 48～64  
### 収集条件（当院 LMEGP）  
- 収集エネルギー　-> 159keV(20% -> lo648wlimit=143.10000610352; uplimit=174.89999389)  
- マトリクスサイズ -> 128 * 128  
- 収集角度 -> 360度  
- 収集時間 -> 24時間 = 30s/step  
- 収集ステップ数 -> 72  
- zoom -> 1.45 (3.2956700325012mm)
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
画像またはスペクトルのコンポーネントを分離する "penetrate" スコアリングルーチンに関して。    
18 種類の異なる画像とエネルギースペクトルが保存されています。  
画像のファイル名は拡張子 .b01 から .b18 までで保存されます。異なるエネルギースペクトルは連続した順序で .bis ファイルに保存されます。スコアリングルーチンは、Index 84=4 を選択して実行されます。異なる画像ファイルとスペクトルは、以下の表に従って分離されます。  
イベントの発生源は次のように示されます。  
.b01 = あらゆる種類の相互作用。  
.b18 = ファントム内での散乱と減衰のない光子。  
.b19 = ファントム内での散乱と減衰のない光子で幾何学的にコリメートされ、主要な光子エネルギーを使用（.isd ファイルで負のエネルギーで示されます）。  
  
結晶の後ろの区画からのバックスキャッターがない次のファイルには、次のようなイベントが表示されます。  
.b02 = ファントムからの主要な減衰した光子の幾何学的にコリメートされたもの。  
.b03 = ファントムからの主要な減衰した光子によるセプタの貫通。  
.b04 = コリメーターからの主要な減衰した光子の散乱。  
.b05 = コリメーターからの X 線。  
.b06 = ファントムからの散乱光子の幾何学的にコリメートされたもの。  
.b07 = ファントムからの散乱光子によるセプタの貫通。  
.b08 = コリメーターからの散乱光子の散乱。  
.b09 = コリメーターからの散乱光子の X 線。  
結晶の後ろの区画からのバックスキャッターがある次のものは、次のようなイベントが表示されます。  
.b10 = ファントムからの主要な減衰した光子の幾何学的にコリメートされたもの。  
.b11 = ファントムからの主要な減衰した光子によるセプタの貫通。  
.b12 = コリメーターからの主要な減衰した光子の散乱。  
.b13 = コリメーターからの主要な減衰した光子の X 線。  
.b14 = ファントムからの散乱光子の幾何学的にコリメートされたもの。  
.b15 = ファントムからの散乱光子によるセプタの貫通。  
.b16 = コリメーターからの散乱光子の散乱。  
.b17 = コリメーターからの散乱光子の X 線。  
エネルギースペクトルファイルの内容は、上記の出現順序に従いますが、異なるスペクトルは単一のファイルに保存されます。.bis ファイルにアクセスするには、ファイルを開き、スペクトルに従って2次元の32ビット浮動小数点ベクトルに読み込みます（NrChannels、18）。NrChannels の値は Index 80 で定義されます。同じ数字を使用して適切なエネルギースペクトルを選択できます。例えば、ファントム内で散乱した光子からのイベントの分布は、spectra(*,8) としてプロットされます。

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

