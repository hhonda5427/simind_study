


              SIMIND Monte Carlo Simulation Program    V7.0.3
------------------------------------------------------------------------------
 Phantom(S): h2o       Crystal...: nai       InputFile.: symbia            
 Phantom(B): bone      BackScatt.: pmt       OutputFile: me_up             
 Collimator: pb_sb2    SourceRout: jaszak    SourceFile: none              
 Cover.....: al        ScoreRout.: penetrate DensityMap: none              
------------------------------------------------------------------------------
 PhotonEnergy.......: 159          i123     PhotonsPerProj....: 20000000       
 EnergyResolution...: 0            sy-me    Activity..........: 1              
 MaxScatterOrder....: 3            SPECT    DetectorLenght....: 22.25          
 DetectorWidth......: 29.55        BScatt   DetectorHeight....: 0.95           
 UpperEneWindowTresh: 194.775      Random   Distance to det...: 15             
 LowerEneWindowTresh: 170.925      Cover    ShiftSource X.....: 0              
 PixelSize  I.......: 0.4          Phantom  ShiftSource Y.....: 0              
 PixelSize  J.......: 0.4          Resolut  ShiftSource Z.....: 0              
 HalfLength S.......: 0.1          Header   HalfLength P......: 10             
 HalfWidth  S.......: 0.1          SaveMap  HalfWidth  P......: 11             
 HalfHeight S.......: 0.1                   HalfHeight P......: 11             
 SourceType.........: MultiSphere           PhantomType.......: HorCylinder  
------------------------------------------------------------------------------
 GENERAL DATA
 keV/channel........: 1                     CutoffEnergy......: 0              
 Photons/Bq.........: 1.72885               StartingAngle.....: 0              
 CameraOffset X.....: 0                     CoverThickness....: 0.1            
 CameraOffset Y.....: 0                     BackscatterThickn.: 7.5            
 MatrixSize I.......: 128                   IntrinsicResolut..: 0.38           
 MatrixSize J.......: 128                   AcceptanceAngle...: 85.58914       
 Emission type......: 3                     Initial Weight....: 0.08644        
 NN ScalingFactor...: 1                     Energy Channels...: 512            
------------------------------------------------------------------------------
 SPECT DATA
 RotationMode.......: -360                  Nr of Projections.: 120            
 RotationAngle......: 3                     Projection.[start]: 1              
 Orbital fraction...: 1                     Projection...[end]: 120            
------------------------------------------------------------------------------
 COLLIMATOR DATA FOR ROUTINE: MC RayTracing       
 CollimatorCode.....: sy-me                 CollimatorType....: Parallel 
 HoleSize X.........: 0.294                 Distance X........: 0.114          
 HoleSize Y.........: 0.33948               Distance Y........: 0.26847        
 CenterShift X......: 0.35334               X-Ray flag........: F              
 CenterShift Y......: 0.204                 CollimThickness...: 4.064          
 HoleShape..........: Hexagonal             Space Coll2Det....: 0              
 CollDepValue [57]..: 0                     CollDepValue [58].: 0              
 CollDepValue [59]..: 1                     CollDepValue [60].: 0              
------------------------------------------------------------------------------
 MULTIPLE SOURCE CONFIGURATION

 Source   Volume(ml)    MBq      kBq/ml      Shape
    1        0.5236    0.0109    0.0209  Ellipsoid           
    2        1.1503    0.0240    0.0209  Ellipsoid           
    3        2.5724    0.0538    0.0209  Ellipsoid           
    4        5.5753    0.1165    0.0209  Ellipsoid           
    5       11.4940    0.2403    0.0209  Ellipsoid           
    6       26.5218    0.5544    0.0209  Ellipsoid           
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
PENETRATE ROUTINE -   B=BackScatter, P=PhantomScatter

                       Energy Window %      :      Total Spectrum %
                 -B,-P  -B,+P  +B,-P   +B+P  -B,-P  -B,+P  +B,-P   +B+P
 geometric....:  20.88   4.08   1.34   0.75  21.30  44.07   1.80   1.06
 penetration..:   2.86   0.91  28.49   6.41   4.11   2.28   7.26   1.67
 collim scatt.:   4.40   1.24  23.64   5.01   6.12   2.58   6.33   1.42
 collim x-rays:   0.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00
------------------------------------------------------------------------------
 INTERACTIONS IN THE CRYSTAL
 MaxValue spectrum..: 313.6          
 MaxValue projection: 0.5295E-01     
 CountRate spectrum.: 180.0          
 CountRate E-Window.: 6.237          
------------------------------------------------------------------------------
 PHOTONS AFTER COLLIMATOR AND WITHIN ENER-WIN
 Geometric..........:  67.67 %          27.05 %
 Penetration........:  17.03 %          38.67 %
 Scatter in collim..:  15.31 %          34.28 %
 X-rays in collim...:   0.00 %           0.00 %
------------------------------------------------------------------------------
 SCATTER IN ENERGY WINDOW
 Scatter/Primary....: 0.22533        
 Scatter/Total......: 0.1839         
 Scatter order 1....: 81.10 %        
 Scatter order 2....: 14.93 %        
 Scatter order 3....: 3.98 %         
------------------------------------------------------------------------------
 CALCULATED DETECTOR PARAMETERS
 Efficiency E-Window: 0.0223         
 Efficiency spectrum: 0.6427         
 Sensitivity Cps/MBq: 6.2367         
 Sensitivity Cpm/uCi: 13.8456        
------------------------------------------------------------------------------
 Simulation started.: 2024:01:22 07:45:59
 Simulation stopped.: 2024:01:22 11:14:54
 Elapsed time.......: 3 h, 28 m and 55 s
 DetectorHits.......: 699897         
 DetectorHits/CPUsec: 238            
------------------------------------------------------------------------------
 SIMIND built 2022:11:25 with INTEL Win    compiler
 Random number generator: ranmar
 Comment:EMISSION
 Energy resolution file:symbia.erf
 Energy resolution (keV) fitted to the function
 er=a+b*sqrt(E+c*E^2)
 where a,b and c are set to -0.534,0.946 and 0.006
 Header file: me_up.h00
 Flat-to-Flat 45 degrees rotated for hex hole
 Inifile: simind.ini
 Message: Input file used is:symbia.inp                                        
 Command: symbia me_up/fi:i123/20:194.775/21:170.925/fe:symbia.erf/CC:sy-me/53:1/59:1/84:4
