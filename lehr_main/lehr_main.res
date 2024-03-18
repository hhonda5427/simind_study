


              SIMIND Monte Carlo Simulation Program    V7.0.3
------------------------------------------------------------------------------
 Phantom(S): h2o       Crystal...: nai       InputFile.: symbia            
 Phantom(B): bone      BackScatt.: pmt       OutputFile: lehr_main         
 Collimator: pb_sb2    SourceRout: jaszak    SourceFile: none              
 Cover.....: al        ScoreRout.: penetrate DensityMap: none              
------------------------------------------------------------------------------
 PhotonEnergy.......: 159          i123     PhotonsPerProj....: 100000000      
 EnergyResolution...: 0            sy-lehr  Activity..........: 1              
 MaxScatterOrder....: 6            SPECT    DetectorLenght....: 22.25          
 DetectorWidth......: 29.55        Xrays    DetectorHeight....: 0.95           
 UpperEneWindowTresh: 170.925      BScatt   Distance to det...: 15             
 LowerEneWindowTresh: 147.075      Random   ShiftSource X.....: 0              
 PixelSize  I.......: 0.22         Cover    ShiftSource Y.....: 0              
 PixelSize  J.......: 0.22         Phantom  ShiftSource Z.....: 0              
 HalfLength S.......: 0.1          Resolut  HalfLength P......: 9.3            
 HalfWidth  S.......: 0.1          Header   HalfWidth  P......: 10.8           
 HalfHeight S.......: 0.1          SaveMap  HalfHeight P......: 10.8           
 SourceType.........: MultiSphere           PhantomType.......: HorCylinder  
------------------------------------------------------------------------------
 GENERAL DATA
 keV/channel........: 2                     CutoffEnergy......: 0              
 Photons/Bq.........: 1.72885               StartingAngle.....: 0              
 CameraOffset X.....: 0                     CoverThickness....: 0.1            
 CameraOffset Y.....: 0                     BackscatterThickn.: 7.5            
 MatrixSize I.......: 256                   IntrinsicResolut..: 0.38           
 MatrixSize J.......: 256                   AcceptanceAngle...: 85.31432       
 Emission type......: 3                     Initial Weight....: 0.01729        
 NN ScalingFactor...: 1                     Energy Channels...: 512            
------------------------------------------------------------------------------
 SPECT DATA
 RotationMode.......: -360                  Nr of Projections.: 120            
 RotationAngle......: 3                     Projection.[start]: 1              
 Orbital fraction...: 1                     Projection...[end]: 120            
------------------------------------------------------------------------------
 COLLIMATOR DATA FOR ROUTINE: MC RayTracing       
 CollimatorCode.....: sy-lehr               CollimatorType....: Parallel 
 HoleSize X.........: 0.111                 Distance X........: 0.016          
 HoleSize Y.........: 0.12817               Distance Y........: 0.07794        
 CenterShift X......: 0.10999               X-Ray flag........: T              
 CenterShift Y......: 0.0635                CollimThickness...: 2.405          
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
 geometric....:  24.34   8.25   0.06   0.05   3.09   8.18   0.26   0.15
 penetration..:   9.37   3.24  22.94  11.52  21.15   9.93  20.95   7.88
 collim scatt.:   4.89   1.77   9.21   4.36   9.63   4.90   6.88   2.78
 collim x-rays:   0.00   0.00   0.00   0.00   2.39   1.82   0.00   0.00
------------------------------------------------------------------------------
 INTERACTIONS IN THE CRYSTAL
 MaxValue spectrum..: 894.5          
 MaxValue projection: 0.1141         
 CountRate spectrum.: 775.9          
 CountRate E-Window.: 74.09          
------------------------------------------------------------------------------
 PHOTONS AFTER COLLIMATOR AND WITHIN ENER-WIN
 Geometric..........:  13.42 %          32.70 %
 Penetration........:  60.70 %          47.07 %
 Scatter in collim..:  23.38 %          20.23 %
 X-rays in collim...:   2.50 %           0.00 %

 K-edge 87.6 keV
 K-hv1  75.0 keV  42.33 %   0.00 %
 K-hv2  72.8 keV  23.28 %   0.00 %
 K-hv3  84.9 keV  15.42 %   0.00 %
 K-hv4  84.4 keV   7.88 %   0.00 %
 K-hv5  87.3 keV   6.41 %   0.00 %
 K-hv6  85.5 keV   0.46 %   0.00 %
 K-hv7  87.6 keV   0.15 %   0.00 %
 K-hv8  72.1 keV   4.07 %   0.00 %
------------------------------------------------------------------------------
 SCATTER IN ENERGY WINDOW
 Scatter/Primary....: 0.41217        
 Scatter/Total......: 0.29187        
 Scatter order 1....: 83.72 %        
 Scatter order 2....: 14.12 %        
 Scatter order 3....: 1.87 %         
 Scatter order 4....: 0.24 %         
 Scatter order 5....: 0.03 %         
 Scatter order 6....: 0.01 %         
------------------------------------------------------------------------------
 CALCULATED DETECTOR PARAMETERS
 Efficiency E-Window: 0.0459         
 Efficiency spectrum: 0.4804         
 Sensitivity Cps/MBq: 74.0938        
 Sensitivity Cpm/uCi: 164.4883       
------------------------------------------------------------------------------
 Simulation started.: 2024:01:28 18:02:16
 Simulation stopped.: 2024:01:29 17:45:55
 Elapsed time.......: 23 h, 43 m and 39 s
 DetectorHits.......: 5955011        
 DetectorHits/CPUsec: 182            
------------------------------------------------------------------------------
 SIMIND built 2022:11:25 with INTEL Win    compiler
 Random number generator: ranmar
 Comment:EMISSION
 Energy resolution file:symbia.erf
 Energy resolution (keV) fitted to the function
 er=a+b*sqrt(E+c*E^2)
 where a,b and c are set to -0.534,0.946 and 0.006
 Header file: lehr_main.h00
 Flat-to-Flat 45 degrees rotated for hex hole
 Inifile: simind.ini
 Message: Input file used is:symbia.inp                                        
 Command: symbia lehr_main/fi:i123/20:170.925/21:147.075/fe:symbia.erf/CC:sy-lehr/53:1/59:1/in:x22,3x/sc:6
