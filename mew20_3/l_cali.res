


              SIMIND Monte Carlo Simulation Program    V7.0.3
------------------------------------------------------------------------------
 Phantom(S): h2o       Crystal...: nai       InputFile.: symbia            
 Phantom(B): h2o       BackScatt.: pmt       OutputFile: l_cali            
 Collimator: pb_sb2    SourceRout: none      SourceFile: none              
 Cover.....: al        ScoreRout.: penetrate DensityMap: none              
------------------------------------------------------------------------------
 PhotonEnergy.......: 159          i123     PhotonsPerProj....: 100000000      
 EnergyResolution...: 0            sy-lehr  Activity..........: 1              
 MaxScatterOrder....: 0            SPECT    DetectorLenght....: 22.25          
 DetectorWidth......: 29.55        Xrays    DetectorHeight....: 0.95           
 UpperEneWindowTresh: 174.9        BScatt   Distance to det...: 15             
 LowerEneWindowTresh: 143.1        Random   ShiftSource X.....: 0              
 PixelSize  I.......: 0.32957      Cover    ShiftSource Y.....: 0              
 PixelSize  J.......: 0.32957      Resolut  ShiftSource Z.....: 0              
 HalfLength S.......: 0                     HalfLength P......: 9.3            
 HalfWidth  S.......: 0                     HalfWidth  P......: 10.8           
 HalfHeight S.......: 0                     HalfHeight P......: 10.8           
 SourceType.........: PointSrc              PhantomType.......: HorCylinder  
------------------------------------------------------------------------------
 GENERAL DATA
 keV/channel........: 1                     CutoffEnergy......: 0              
 Photons/Bq.........: 1.72885               StartingAngle.....: 0              
 CameraOffset X.....: 0                     CoverThickness....: 0.1            
 CameraOffset Y.....: 0                     BackscatterThickn.: 7.5            
 MatrixSize I.......: 128                   IntrinsicResolut..: 0.38           
 MatrixSize J.......: 128                   AcceptanceAngle...: 67.92674       
 Emission type......: 3                     Initial Weight....: 0.01729        
 NN ScalingFactor...: 1                     Energy Channels...: 512            
------------------------------------------------------------------------------
 SPECT DATA
 RotationMode.......: -360                  Nr of Projections.: 1              
 RotationAngle......: 360                   Projection.[start]: 1              
 Orbital fraction...: 1                     Projection...[end]: 1              
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
 geometric....:  39.07   0.00   0.09   0.00  12.44   0.00   0.61   0.00
 penetration..:  13.63   0.00  29.38   0.00  22.21   0.00  34.63   0.00
 collim scatt.:   6.93   0.00  10.90   0.00  14.42   0.00  11.21   0.00
 collim x-rays:   0.00   0.00   0.00   0.00   4.48   0.00   0.00   0.00
------------------------------------------------------------------------------
 INTERACTIONS IN THE CRYSTAL
 MaxValue spectrum..: 13.04          
 MaxValue projection: 7.193          
 CountRate spectrum.: 1172.          
 CountRate E-Window.: 180.3          
------------------------------------------------------------------------------
 PHOTONS AFTER COLLIMATOR AND WITHIN ENER-WIN
 Geometric..........:   6.59 %          39.16 %
 Penetration........:  67.47 %          43.01 %
 Scatter in collim..:  23.92 %          17.83 %
 X-rays in collim...:   2.01 %           0.00 %

 K-edge 87.6 keV
 K-hv1  75.0 keV  43.85 %   0.00 %
 K-hv2  72.8 keV  24.88 %   0.00 %
 K-hv3  84.9 keV  15.75 %   0.00 %
 K-hv4  84.4 keV   8.32 %   0.00 %
 K-hv5  87.3 keV   6.53 %   0.00 %
 K-hv6  85.5 keV   0.49 %   0.00 %
 K-hv7  87.6 keV   0.13 %   0.00 %
 K-hv8  72.1 keV   0.04 %   0.00 %
------------------------------------------------------------------------------
 CALCULATED DETECTOR PARAMETERS
 Efficiency E-Window: 0.0625         
 Efficiency spectrum: 0.4065         
 Sensitivity Cps/MBq: 180.2658       
 Sensitivity Cpm/uCi: 400.1901       
------------------------------------------------------------------------------
 Simulation started.: 2024:04:12 14:46:04
 Simulation stopped.: 2024:04:12 14:48:07
 Elapsed time.......: 0 h, 2 m and 3 s
 DetectorHits.......: 1775170        
 DetectorHits/CPUsec: 77024          
------------------------------------------------------------------------------
 SIMIND built 2022:11:25 with INTEL Win    compiler
 Random number generator: ranmar
 Comment:
 Energy resolution file:symbia.erf
 Energy resolution (keV) fitted to the function
 er=a+b*sqrt(E+c*E^2)
 where a,b and c are set to -0.534,0.946 and 0.006
 Flat-to-Flat 45 degrees rotated for hex hole
 Inifile: simind.ini
 Command: symbia l_cali/fi:i123/fe:symbia.erf/CC:sy-lehr/53:1/59:1/in:x22,3x/sc:4/29:1/15:5/fa:11/fa:15/fa:14
