


              SIMIND Monte Carlo Simulation Program    V7.0.3
------------------------------------------------------------------------------
 Phantom(S): h2o       Crystal...: nai       InputFile.: mibg              
 Phantom(B): bone      BackScatt.: lucite    OutputFile: mibg              
 Collimator: pb_sb2    SourceRout: smap      SourceFile: vox_man           
 Cover.....: al        ScoreRout.: scattwin  DensityMap: vox_man           
------------------------------------------------------------------------------
 PhotonEnergy.......: 159          i123     PhotonsPerProj....: 459861000      
 EnergyResolution...: 0            sy-lehr  Activity..........: 1              
 MaxScatterOrder....: 4            SPECT    DetectorLenght....: 20             
 DetectorWidth......: 25           Random   DetectorHeight....: 0.953          
 UpperEneWindowTresh: 174.9        Cover    Distance to det...: 25             
 LowerEneWindowTresh: 143.1        Phantom  ShiftSource X.....: 0              
 PixelSize  I.......: 0.315        Resolut  ShiftSource Y.....: 0              
 PixelSize  J.......: 0.315        Header   ShiftSource Z.....: 0              
 HalfLength S.......: 25           SaveMap  HalfLength P......: 25             
 HalfWidth  S.......: 0                     HalfWidth  P......: 0              
 HalfHeight S.......: 0                     HalfHeight P......: 0              
 SourceType.........: ZubalVoxMan           PhantomType.......: ZubalVoxMan  
------------------------------------------------------------------------------
 GENERAL DATA
 keV/channel........: 1                     CutoffEnergy......: 0              
 Photons/Bq.........: 1.72885               StartingAngle.....: 0              
 CameraOffset X.....: 0                     CoverThickness....: 0.1            
 CameraOffset Y.....: 0                     BackscatterThickn.: 0              
 MatrixSize I.......: 128                   IntrinsicResolut..: 0.38           
 MatrixSize J.......: 128                   AcceptanceAngle...: 66.32369       
 Emission type......: 3                     Initial Weight....: 0.00376        
 NN ScalingFactor...: 200                   Energy Channels...: 512            
------------------------------------------------------------------------------
 SPECT DATA
 RotationMode.......: -360                  Nr of Projections.: 64             
 RotationAngle......: 5.625                 Projection.[start]: 1              
 Orbital fraction...: 1                     Projection...[end]: 64             
------------------------------------------------------------------------------
 COLLIMATOR DATA FOR ROUTINE: MC RayTracing       
 CollimatorCode.....: sy-lehr               CollimatorType....: Parallel 
 HoleSize X.........: 0.111                 Distance X........: 0.016          
 HoleSize Y.........: 0.12817               Distance Y........: 0.07794        
 CenterShift X......: 0.10999               X-Ray flag........: F              
 CenterShift Y......: 0.0635                CollimThickness...: 2.405          
 HoleShape..........: Hexagonal             Space Coll2Det....: 0              
 CollDepValue [57]..: 0                     CollDepValue [58].: 0              
 CollDepValue [59]..: 1                     CollDepValue [60].: 0              
------------------------------------------------------------------------------
 IMAGE-BASED PHANTOM DATA
 RotationCentre.....:  65, 65               Bone definition...: 1170           
 CT-Pixel size......: 0.34                  Slice thickness...: 0.35714        
 StartImage.........: 80                    No of CT-Images...: 140            
 MatrixSize I.......: 128                   CTmapOrientation..: 0              
 MatrixSize J.......: 128                   StepSize..........: 0.2            
 CenterPoint I......: 65                    ShiftPhantom X....: 0              
 CenterPoint J......: 65                    ShiftPhantom Y....: 0              
 CenterPoint K......: 71                    ShiftPhantom Z....: 0              
------------------------------------------------------------------------------
 PHANTOM DATA FROM FILE: mibg.zub section: 1

 Code Volume          Density   Voxels Volume(mL)        MBq     MBq/mL   Value
   1: skin              1.090   211449  0.873E+04  0.920E-01  0.105E-01   1.000
   3: spinal cord       1.038     2760  0.114E+03  0.120E-02  0.105E-01   1.000
   5: spine             1.330    12796  0.528E+03  0.557E-02  0.105E-01   1.000
   6: rib cage & ster   1.410    22418  0.926E+03  0.975E-02  0.105E-01   1.000
   7: pelvis            1.290    13513  0.558E+03  0.588E-02  0.105E-01   1.000
   8: long bones        1.330     4439  0.183E+03  0.193E-02  0.105E-01   1.000
   9: skeletal muscle   1.050   210913  0.871E+04  0.917E-01  0.105E-01   1.000
  10: lungs             0.260    54631  0.226E+04  0.238E+00  0.105E+00  10.000
  11: heart             1.060     9354  0.386E+03  0.407E-02  0.105E-01   1.000
  12: liver             1.060    30192  0.125E+04  0.263E+00  0.211E+00  20.000
  13: gall bladder      1.026      329  0.136E+02  0.143E-03  0.105E-01   1.000
  14: kidney            1.050     7618  0.315E+03  0.331E-01  0.105E+00  10.000
  16: esophagus         1.030      468  0.193E+02  0.204E-03  0.105E-01   1.000
  17: stomach           1.030     5133  0.212E+03  0.223E-02  0.105E-01   1.000
  18: small bowel       1.030    26447  0.109E+04  0.690E-01  0.632E-01   6.000
  19: colon             1.030    18284  0.755E+03  0.477E-01  0.632E-01   6.000
  20: pancreas          1.040      792  0.327E+02  0.344E-03  0.105E-01   1.000
  21: adrenals          1.025       62  0.256E+01  0.135E-03  0.527E-01   5.000
  23: blood pool        1.060    14157  0.584E+03  0.616E-02  0.105E-01   1.000
  24: gas (bowel)       0.260     3167  0.131E+03  0.138E-02  0.105E-01   1.000
  25: fluid (bowel)     1.007      528  0.218E+02  0.230E-03  0.105E-01   1.000
  26: bone marrow       1.030    15861  0.655E+03  0.690E-02  0.105E-01   1.000
  29: trachea           1.000       74  0.306E+01  0.322E-04  0.105E-01   1.000
  31: spleen            1.060     5568  0.230E+03  0.484E-01  0.211E+00  20.000
  32: urine             1.030     6597  0.272E+03  0.230E-01  0.843E-01   8.000
  33: feces             1.010     1134  0.468E+02  0.493E-03  0.105E-01   1.000
  34: testes            1.040      201  0.830E+01  0.874E-04  0.105E-01   1.000
  35: prostate          1.045      400  0.165E+02  0.174E-03  0.105E-01   1.000
  37: rectum            1.030     1363  0.563E+02  0.593E-03  0.105E-01   1.000
  39: diaphragm         1.030     4528  0.187E+03  0.197E-02  0.105E-01   1.000
  40: bladder           1.040     3147  0.130E+03  0.342E-01  0.263E+00  25.000
 TUMORS FROM FILE:mibg.inp                                                    
 Tumor  Vol(pix)     Vol(cc)     MBq        MBq/cc   CHANGE g/cm3
   1      925      0.382E+02   0.121E-01   0.316E-03    5.000
------------------------------------------------------------------------------
  Photon energy       Abundance
     27.202 keV       0.2469    
     27.473 keV       0.4598    
     31.104 keV       0.1316    
     31.762 keV       0.2860E-01
    158.970 keV       0.8325    
    174.200 keV       0.8300E-05
    182.610 keV       0.1800E-03
    192.170 keV       0.1990E-03
    197.220 keV       0.3300E-05
    198.230 keV       0.3500E-04
    206.790 keV       0.3300E-04
    207.800 keV       0.1120E-04
    247.960 keV       0.6980E-03
    257.510 keV       0.1600E-04
    278.360 keV       0.2300E-04
    281.030 keV       0.7890E-03
    295.170 keV       0.1582E-04
    329.380 keV       0.2600E-04
    330.700 keV       0.1164E-03
    343.730 keV       0.4400E-04
    346.350 keV       0.1257E-02
    405.020 keV       0.2980E-04
    437.500 keV       0.7000E-05
    440.020 keV       0.4229E-02
    454.760 keV       0.4120E-04
    505.330 keV       0.2660E-02
    528.960 keV       0.1280E-01
    538.540 keV       0.3788E-02
    556.050 keV       0.2900E-04
    562.790 keV       0.1150E-04
    578.260 keV       0.1260E-04
    599.690 keV       0.2660E-04
    610.050 keV       0.1100E-04
    624.570 keV       0.7980E-03
    628.260 keV       0.1640E-04
    687.950 keV       0.2690E-03
    735.780 keV       0.6160E-03
    783.590 keV       0.5910E-03
    837.100 keV       0.5820E-05
    877.520 keV       0.8300E-05
    894.800 keV       0.1010E-04
    909.120 keV       0.1410E-04
   1036.630 keV       0.9700E-05
   1068.120 keV       0.1420E-04
------------------------------------------------------------------------------
  Scattwin results: Window file: mibg.win            
  
  Win  WinAdded  Range(keV)   ScaleFactor
   1       0    147.1 - 170.9    1.00
   2       0    123.2 - 147.1    1.00
   3       0    170.9 - 194.8    1.00
  
  Win    Total    Scatter   Primary  S/P-Ratio S/T Ratio  Cps/MBq
   1   0.207E+04 0.505E+03 0.156E+04 0.323E+00 0.244E+00 0.323E+02
   2   0.120E+04 0.788E+03 0.413E+03 0.191E+01 0.656E+00 0.188E+02
   3   0.503E+03 0.153E+03 0.350E+03 0.437E+00 0.304E+00 0.786E+01
  
  Win  Geo(Air)  Pen(Air)  Sca(Air)  Geo(Tot)  Pen(Tot)  Sca(Tot)
   1    64.43%    25.29%    10.28%    59.42%    28.82%    11.75%
   2    19.55%    57.18%    23.27%    53.20%    33.15%    13.65%
   3    17.68%    58.55%    23.77%    10.01%    63.01%    26.98%
  
  Win   SC 1  SC 2  SC 3  SC 4
   1   84.8% 12.7%  2.0%  0.5%
   2   66.4% 26.2%  6.2%  1.2%
   3   74.3% 19.2%  5.1%  1.4%
------------------------------------------------------------------------------
 INTERACTIONS IN THE CRYSTAL
 MaxValue spectrum..: 115.4          
 MaxValue projection: 0.1501E-01     
 CountRate spectrum.: 278.6          
 CountRate E-Window.: 37.85          
------------------------------------------------------------------------------
 PHOTONS AFTER COLLIMATOR AND WITHIN ENER-WIN
 Geometric..........:  15.84 %          57.50 %
 Penetration........:  62.81 %          30.14 %
 Scatter in collim..:  21.35 %          12.36 %
 X-rays in collim...:   0.00 %           0.00 %
------------------------------------------------------------------------------
 SCATTER IN ENERGY WINDOW
 Scatter/Primary....: 0.37942        
 Scatter/Total......: 0.27506        
 Scatter order 1....: 83.13 %        
 Scatter order 2....: 14.08 %        
 Scatter order 3....: 2.29 %         
 Scatter order 4....: 0.49 %         
------------------------------------------------------------------------------
 CALCULATED DETECTOR PARAMETERS
 Efficiency E-Window: 0.0385         
 Efficiency spectrum: 0.2833         
 Sensitivity Cps/MBq: 37.8476        
 Sensitivity Cpm/uCi: 84.0217        
------------------------------------------------------------------------------
 Simulation started.: 2024:10:14 05:57:21
 Simulation stopped.: 2024:10:15 14:39:04
 Elapsed time.......: 32 h, 41 m and 43 s
 DetectorHits.......: 17162292       
 DetectorHits/CPUsec: 397            
------------------------------------------------------------------------------
 SIMIND built 2022:11:25 with INTEL Win    compiler
 Random number generator: ranmar
 Comment:EMISSION VMAN
 Energy resolution file:mibg.erf
 Energy resolution (keV) fitted to the function
 er=a+b*sqrt(E+c*E^2)
 where a,b and c are set to -0.534,0.946 and 0.006
 Header file: mibg.h00
 Flat-to-Flat 45 degrees rotated for hex hole
 Inifile: simind.ini
 Command: mibg mibg/fi:i123/fe:mibg.erf/in:x22,3x/sc:4/fz:mibg.zub/if:mibg.inp/nn:200
