


              SIMIND Monte Carlo Simulation Program    V7.0.3
------------------------------------------------------------------------------
 Phantom(S): h2o       Crystal...: nai       InputFile.: symbia            
 Phantom(B): h2o       BackScatt.: pmt       OutputFile: l_low             
 Collimator: pb_sb2    SourceRout: jaszak    SourceFile: none              
 Cover.....: al        ScoreRout.: penetrate DensityMap: none              
------------------------------------------------------------------------------
 PhotonEnergy.......: 159          i123     PhotonsPerProj....: 100000000      
 EnergyResolution...: 0            sy-lehr  Activity..........: 1              
 MaxScatterOrder....: 4            SPECT    DetectorLenght....: 22.25          
 DetectorWidth......: 29.55        Xrays    DetectorHeight....: 0.95           
 UpperEneWindowTresh: 143.1        BScatt   Distance to det...: 15             
 LowerEneWindowTresh: 138.33       Random   ShiftSource X.....: 0              
 PixelSize  I.......: 0.32957      Cover    ShiftSource Y.....: 0              
 PixelSize  J.......: 0.32957      Phantom  ShiftSource Z.....: 0              
 HalfLength S.......: 0.1          Resolut  HalfLength P......: 9.3            
 HalfWidth  S.......: 0.1          Header   HalfWidth  P......: 10.8           
 HalfHeight S.......: 0.1          SaveMap  HalfHeight P......: 10.8           
 SourceType.........: MultiSphere           PhantomType.......: HorCylinder  
------------------------------------------------------------------------------
 GENERAL DATA
 keV/channel........: 1                     CutoffEnergy......: 0              
 Photons/Bq.........: 1.72885               StartingAngle.....: 0              
 CameraOffset X.....: 0                     CoverThickness....: 0.1            
 CameraOffset Y.....: 0                     BackscatterThickn.: 7.5            
 MatrixSize I.......: 128                   IntrinsicResolut..: 0.38           
 MatrixSize J.......: 128                   AcceptanceAngle...: 85.31432       
 Emission type......: 3                     Initial Weight....: 0.01729        
 NN ScalingFactor...: 1                     Energy Channels...: 512            
------------------------------------------------------------------------------
 SPECT DATA
 RotationMode.......: -360                  Nr of Projections.: 72             
 RotationAngle......: 5                     Projection.[start]: 1              
 Orbital fraction...: 1                     Projection...[end]: 72             
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
    1        4.1888    0.0028    0.0007  Ellipsoid           
    2        8.1812    0.0055    0.0007  Ellipsoid           
    3       14.1372    0.0095    0.0007  Ellipsoid           
    4       22.4493    0.0152    0.0007  Ellipsoid           
    5       33.5103    0.0226    0.0007  Ellipsoid           
    6       65.4498    0.0442    0.0007  Ellipsoid           
  BKG     6665.0000    0.9001    0.0001
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
 geometric....:   3.28  18.84   0.17   0.08   4.71   6.24   0.34   0.13
 penetration..:   5.76   3.53  33.57  10.91  16.55   7.61  26.59   6.60
 collim scatt.:   4.15   2.00  13.23   4.47  11.17   3.98   8.97   2.33
 collim x-rays:   0.00   0.00   0.00   0.00   3.22   1.56   0.00   0.00
------------------------------------------------------------------------------
 INTERACTIONS IN THE CRYSTAL
 MaxValue spectrum..: 304.7          
 MaxValue projection: 0.2016E-01     
 CountRate spectrum.: 762.3          
 CountRate E-Window.: 9.899          
------------------------------------------------------------------------------
 PHOTONS AFTER COLLIMATOR AND WITHIN ENER-WIN
 Geometric..........:  11.23 %          22.38 %
 Penetration........:  62.38 %          53.77 %
 Scatter in collim..:  23.94 %          23.85 %
 X-rays in collim...:   2.45 %           0.00 %

 K-edge 87.6 keV
 K-hv1  75.0 keV  42.97 %   0.00 %
 K-hv2  72.8 keV  23.62 %   0.00 %
 K-hv3  84.9 keV  15.63 %   0.00 %
 K-hv4  84.4 keV   8.00 %   0.00 %
 K-hv5  87.3 keV   6.46 %   0.00 %
 K-hv6  85.5 keV   0.47 %   0.00 %
 K-hv7  87.6 keV   0.15 %   0.00 %
 K-hv8  72.1 keV   2.71 %   0.00 %
------------------------------------------------------------------------------
 SCATTER IN ENERGY WINDOW
 Scatter/Primary....: 0.66222        
 Scatter/Total......: 0.39839        
 Scatter order 1....: 78.02 %        
 Scatter order 2....: 18.69 %        
 Scatter order 3....: 2.90 %         
 Scatter order 4....: 0.38 %         
------------------------------------------------------------------------------
 CALCULATED DETECTOR PARAMETERS
 Efficiency E-Window: 0.0054         
 Efficiency spectrum: 0.4197         
 Sensitivity Cps/MBq: 9.8992         
 Sensitivity Cpm/uCi: 21.9763        
------------------------------------------------------------------------------
 Simulation started.: 2024:04:11 17:21:25
 Simulation stopped.: 2024:04:12 04:03:18
 Elapsed time.......: 10 h, 41 m and 53 s
 DetectorHits.......: 4637635        
 DetectorHits/CPUsec: 292            
------------------------------------------------------------------------------
 SIMIND built 2022:11:25 with INTEL Win    compiler
 Random number generator: ranmar
 Comment:EMISSION
 Energy resolution file:symbia.erf
 Energy resolution (keV) fitted to the function
 er=a+b*sqrt(E+c*E^2)
 where a,b and c are set to -0.534,0.946 and 0.006
 Header file: l_low.h00
 Flat-to-Flat 45 degrees rotated for hex hole
 Inifile: simind.ini
 Message: Input file used is:symbia.inp                                        
 Command: symbia l_low/fi:i123/fe:symbia.erf/CC:sy-lehr/53:1/59:1/in:x22,3x/sc:4/20:143.1/21:138.33/bg:0.2