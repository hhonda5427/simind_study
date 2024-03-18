


              SIMIND Monte Carlo Simulation Program    V7.0.3
------------------------------------------------------------------------------
 Phantom(S): h2o       Crystal...: nai       InputFile.: symbia            
 Phantom(B): bone      BackScatt.: pmt       OutputFile: lehr_low          
 Collimator: pb_sb2    SourceRout: jaszak    SourceFile: none              
 Cover.....: al        ScoreRout.: penetrate DensityMap: none              
------------------------------------------------------------------------------
 PhotonEnergy.......: 159          i123     PhotonsPerProj....: 100000000      
 EnergyResolution...: 0            sy-lehr  Activity..........: 1              
 MaxScatterOrder....: 6            SPECT    DetectorLenght....: 22.25          
 DetectorWidth......: 29.55        Xrays    DetectorHeight....: 0.95           
 UpperEneWindowTresh: 147.075      BScatt   Distance to det...: 15             
 LowerEneWindowTresh: 123.225      Random   ShiftSource X.....: 0              
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
 geometric....:   2.60  22.94   0.25   0.13   3.09   8.18   0.26   0.15
 penetration..:   5.08   4.06  28.88  13.57  21.14   9.93  20.94   7.88
 collim scatt.:   3.36   2.43  11.15   5.56   9.65   4.91   6.87   2.77
 collim x-rays:   0.00   0.00   0.00   0.00   2.39   1.83   0.00   0.00
------------------------------------------------------------------------------
 INTERACTIONS IN THE CRYSTAL
 MaxValue spectrum..: 891.2          
 MaxValue projection: 0.2574E-01     
 CountRate spectrum.: 776.2          
 CountRate E-Window.: 49.88          
------------------------------------------------------------------------------
 PHOTONS AFTER COLLIMATOR AND WITHIN ENER-WIN
 Geometric..........:  13.42 %          25.92 %
 Penetration........:  60.70 %          51.59 %
 Scatter in collim..:  23.38 %          22.49 %
 X-rays in collim...:   2.51 %           0.00 %

 K-edge 87.6 keV
 K-hv1  75.0 keV  42.23 %   0.00 %
 K-hv2  72.8 keV  23.30 %   0.00 %
 K-hv3  84.9 keV  15.42 %   0.00 %
 K-hv4  84.4 keV   7.84 %   0.00 %
 K-hv5  87.3 keV   6.40 %   0.00 %
 K-hv6  85.5 keV   0.46 %   0.00 %
 K-hv7  87.6 keV   0.15 %   0.00 %
 K-hv8  72.1 keV   4.20 %   0.00 %
------------------------------------------------------------------------------
 SCATTER IN ENERGY WINDOW
 Scatter/Primary....: 0.94867        
 Scatter/Total......: 0.48683        
 Scatter order 1....: 73.00 %        
 Scatter order 2....: 22.18 %        
 Scatter order 3....: 4.11 %         
 Scatter order 4....: 0.61 %         
 Scatter order 5....: 0.09 %         
 Scatter order 6....: 0.01 %         
------------------------------------------------------------------------------
 CALCULATED DETECTOR PARAMETERS
 Efficiency E-Window: 0.0309         
 Efficiency spectrum: 0.4806         
 Sensitivity Cps/MBq: 49.8816        
 Sensitivity Cpm/uCi: 110.7372       
------------------------------------------------------------------------------
 Simulation started.: 2024:01:29 17:45:56
 Simulation stopped.: 2024:01:30 17:59:33
 Elapsed time.......: 24 h, 13 m and 37 s
 DetectorHits.......: 5954303        
 DetectorHits/CPUsec: 184            
------------------------------------------------------------------------------
 SIMIND built 2022:11:25 with INTEL Win    compiler
 Random number generator: ranmar
 Comment:EMISSION
 Energy resolution file:symbia.erf
 Energy resolution (keV) fitted to the function
 er=a+b*sqrt(E+c*E^2)
 where a,b and c are set to -0.534,0.946 and 0.006
 Header file: lehr_low.h00
 Flat-to-Flat 45 degrees rotated for hex hole
 Inifile: simind.ini
 Message: Input file used is:symbia.inp                                        
 Command: symbia lehr_low/fi:i123/20:147.075/21:123.225/fe:symbia.erf/CC:sy-lehr/53:1/59:1/in:x22,3x/sc:6
