


              SIMIND Monte Carlo Simulation Program    V7.0.3
------------------------------------------------------------------------------
 Phantom(S): h2o       Crystal...: nai       InputFile.: symbia            
 Phantom(B): bone      BackScatt.: pmt       OutputFile: me_calib          
 Collimator: pb_sb2    SourceRout: none      SourceFile: none              
 Cover.....: al        ScoreRout.: penetrate DensityMap: none              
------------------------------------------------------------------------------
 PhotonEnergy.......: 159          i123     PhotonsPerProj....: 20000000       
 EnergyResolution...: 0            sy-me    Activity..........: 1              
 MaxScatterOrder....: 0            SPECT    DetectorLenght....: 22.25          
 DetectorWidth......: 29.55        BScatt   DetectorHeight....: 0.95           
 UpperEneWindowTresh: 170.925      Random   Distance to det...: 15             
 LowerEneWindowTresh: 147.075      Cover    ShiftSource X.....: 0              
 PixelSize  I.......: 0.4          Resolut  ShiftSource Y.....: 0              
 PixelSize  J.......: 0.4          Header   ShiftSource Z.....: 0              
 HalfLength S.......: 0                     HalfLength P......: 10             
 HalfWidth  S.......: 0                     HalfWidth  P......: 11             
 HalfHeight S.......: 0                     HalfHeight P......: 11             
 SourceType.........: PointSrc              PhantomType.......: HorCylinder  
------------------------------------------------------------------------------
 GENERAL DATA
 keV/channel........: 1                     CutoffEnergy......: 0              
 Photons/Bq.........: 1.72885               StartingAngle.....: 0              
 CameraOffset X.....: 0                     CoverThickness....: 0.1            
 CameraOffset Y.....: 0                     BackscatterThickn.: 7.5            
 MatrixSize I.......: 128                   IntrinsicResolut..: 0.38           
 MatrixSize J.......: 128                   AcceptanceAngle...: 67.92674       
 Emission type......: 3                     Initial Weight....: 0.08644        
 NN ScalingFactor...: 1                     Energy Channels...: 512            
------------------------------------------------------------------------------
 SPECT DATA
 RotationMode.......: -360                  Nr of Projections.: 1              
 RotationAngle......: 360                   Projection.[start]: 1              
 Orbital fraction...: 1                     Projection...[end]: 1              
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
 geometric....:  88.32   0.00   0.12   0.00  66.11   0.00   3.07   0.00
 penetration..:   3.74   0.00   2.74   0.00   5.65   0.00   9.00   0.00
 collim scatt.:   2.20   0.00   2.87   0.00   8.13   0.00   8.05   0.00
 collim x-rays:   0.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00
------------------------------------------------------------------------------
 INTERACTIONS IN THE CRYSTAL
 MaxValue spectrum..: 19.18          
 MaxValue projection: 7.216          
 CountRate spectrum.: 366.0          
 CountRate E-Window.: 124.7          
------------------------------------------------------------------------------
 PHOTONS AFTER COLLIMATOR AND WITHIN ENER-WIN
 Geometric..........:  51.81 %          88.45 %
 Penetration........:  25.67 %           6.48 %
 Scatter in collim..:  22.52 %           5.08 %
 X-rays in collim...:   0.00 %           0.00 %
------------------------------------------------------------------------------
 CALCULATED DETECTOR PARAMETERS
 Efficiency E-Window: 0.2171         
 Efficiency spectrum: 0.6374         
 Sensitivity Cps/MBq: 124.6815       
 Sensitivity Cpm/uCi: 276.7929       
------------------------------------------------------------------------------
 Simulation started.: 2024:01:22 11:14:54
 Simulation stopped.: 2024:01:22 11:15:24
 Elapsed time.......: 0 h, 0 m and 30 s
 DetectorHits.......: 260601         
 DetectorHits/CPUsec: 34389          
------------------------------------------------------------------------------
 SIMIND built 2022:11:25 with INTEL Win    compiler
 Random number generator: ranmar
 Comment:STATIC
 Energy resolution file:symbia.erf
 Energy resolution (keV) fitted to the function
 er=a+b*sqrt(E+c*E^2)
 where a,b and c are set to -0.534,0.946 and 0.006
 Header file: me_calib.h00
 Flat-to-Flat 45 degrees rotated for hex hole
 Inifile: simind.ini
 Command: symbia me_calib/fi:i123/20:170.925/21:147.075/fe:symbia.erf/CC:sy-me/53:1/59:1/84:4/29:1/15:5/fa:11/fa:15
