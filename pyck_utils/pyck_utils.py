import math

def SetGeometricParameters(model,L,r,smoothingKernelFunc):
    smoothingLength = 1.3*r*2;
    
    if smoothingKernelFunc != 3:
        Kappa = 2.0;
    else:
        Kappa = 3.0;

    KappaH = smoothingLength*Kappa;
    
    if L[0]==0:
            L[0] = KappaH;
    if L[1]==0:
            L[1] = KappaH;
    if L[2]==0:
            L[2] = KappaH;

    model.SetParameter("Lx","%f" % L[0]);
    model.SetParameter("Ly","%f" % L[1]);
    model.SetParameter("Lz","%f" % L[2]);
    model.SetParameter("GridSizeX","%d" % math.floor(L[0]/KappaH));
    model.SetParameter("GridSizeY","%d" % math.floor(L[1]/KappaH));
    model.SetParameter("GridSizeZ","%d" % math.floor(L[2]/KappaH));
    model.SetParameter("SmoothingLength","%f" % (1.3*r));
    model.SetParameter("InitialParticleSeparation","%f" % (r));

def SetDefaultParameters(model,L,r,smoothingKernelFunc,speedsound, density, shearmodulus, bulkmodulus):
    model.SetParameter("SmoothingKernelFunc","%d" % smoothingKernelFunc);

    if L[2]==0:
            dim = 2;
    else:
            dim = 3;            

    SetGeometricParameters(model,L,r,smoothingKernelFunc);
    model.SetParameter("ParticlesPerCell","100");
    model.SetParameter("MaxSteps","10000");
    model.SetParameter("Mass","1");
    model.SetParameter("Epsilon","0.5");
    model.SetParameter("ViscEtq","0.1");
    model.SetParameter("ViscAlpha","1.0");
    model.SetParameter("ViscBeta","2.0");
    model.SetParameter("DTime","%f" % (0.4*((1.3*r)/speedsound)));
    model.SetParameter("SpeedSound","%f" % speedsound);
    model.SetParameter("InitialDensity","%f" % density);
    model.SetParameter("SmoothingKernelFunc","%d" % smoothingKernelFunc);
    model.SetParameter("Dim","%d" % dim);
    model.SetParameter("AlgorithmSPH","2");
    model.SetParameter("BoundaryUpdateStep","1");
    model.SetParameter("isBoundaryDensityLowLimit","false");
    model.SetParameter("IsExternalForce","false");
    model.SetParameter("IsAverageVelocity","true");
    model.SetParameter("IsVisc","false");
    model.SetParameter("IsViscArtificial","false");
    model.SetParameter("IsNoSlip","false");
    model.SetParameter("IsSurfaceTension","false");
    model.SetParameter("IsDeltaSPH","false");
    model.SetParameter("delta","0.1");
    model.SetParameter("GravityX","0.0");
    model.SetParameter("GravityY","0.0");
    model.SetParameter("GravityZ","0.0");
    model.SetParameter("IsPeriodicBoundaryX","false");
    model.SetParameter("IsPeriodicBoundaryY","false");
    model.SetParameter("IsPeriodicBoundaryZ","false");
    model.SetParameter("IsLaminarVisc","false");
    model.SetParameter("IsSpsVisc","false");
    model.SetParameter("EOS","2");
    model.SetParameter("MonaghanB","");
    model.SetParameter("MonaghanGamma","");
    model.SetParameter("DensityFunction","");
    model.SetParameter("IsRepulsiveForceBC","false");
    model.SetParameter("IsShepard","false");
    model.SetParameter("ShepardStep","");
    model.SetParameter("Viscosity","");
    model.SetParameter("MovingBoundaryAmplitudeX","");
    model.SetParameter("MovingBoundaryAmplitudeY","");
    model.SetParameter("MovingBoundaryAmplitudeZ","");
    model.SetParameter("MovingBoundaryFrequencyX","");
    model.SetParameter("MovingBoundaryFrequencyY","");
    model.SetParameter("MovingBoundaryFrequencyZ","");
    model.SetParameter("MovingBoundaryPhaseX","");
    model.SetParameter("MovingBoundaryPhaseY","");
    model.SetParameter("MovingBoundaryPhaseZ","");
    model.SetParameter("MovingBoundaryShiftX","");
    model.SetParameter("MovingBoundaryShiftY","");
    model.SetParameter("MovingBoundaryShiftZ","");
    model.SetParameter("ShearModulus","%f" % shearmodulus);
    model.SetParameter("BulkModulus","%f" % bulkmodulus);
    model.SetParameter("PoissonRatio","");
    model.SetParameter("YoungModulus","");
    model.SetParameter("deltaRmat","%f" % (1e-12 * 1.667e-05));
    model.SetParameter("yieldTensileStrength","");
    model.SetParameter("KDamage","");
    model.SetParameter("MDamage","");
    model.SetParameter("IsSolids","true");
    model.SetParameter("IsDamage","false");
    model.SetParameter("IsPlasticityCorr","false");
    model.SetParameter("IsTensileInstCorr","false");
    model.SetParameter("IsFlags","false");
    model.SetParameter("IsReverseMoving","false");
    model.SetParameter("IsDensityBound","false");
    model.SetParameter("IsAssociatedFlowRule","false");
    model.SetParameter("IsDPbased","false");
    model.SetParameter("IsDamping","true");
    model.SetParameter("IsAlternateViscArtificial","false");
    model.SetParameter("ViscAlphamin","1.0");
    model.SetParameter("ViscAlphamax","2.5");
    model.SetParameter("IsContactForce","false");
    model.SetParameter("IsForcedBoundaries","false");
    model.SetParameter("IsStressedBoundaries","false");
    model.SetParameter("IsPlaneStress","false");
    model.SetParameter("IsPlaneStrain","false");
    model.SetParameter("IsPlaneStrain2PlaneStress","false");
    model.SetParameter("IsElastoPlasticDamage","false");
    model.SetParameter("IsDruckerPragerPlasticity","false");
    model.SetParameter("DPcohesionSoftening","1");
    model.SetParameter("DPYieldsurface","1");
    model.SetParameter("IsDPApexCriterion","false");
    model.SetParameter("IsDPTensileCrackingCriterion","false");
    model.SetParameter("BoundaryNormalTolerance","0.3");
    model.SetParameter("RankineCriticalStress","");
    model.SetParameter("StVenantCriticalStrain","");
    model.SetParameter("Cohesion","");
    model.SetParameter("FrictionAngle","");
    model.SetParameter("DilatancyAngle","");
    model.SetParameter("YieldShearStrength","");
    model.SetParameter("YieldCompressiveStrength","");
    model.SetParameter("YieldBiaxialCompressiveStrength","");
    model.SetParameter("CohnPt1","");
    model.SetParameter("CohnPt2","");
    model.SetParameter("PlastStrainPt1","");
    model.SetParameter("PlastStrainPt2","");
    model.SetParameter("EpsilonRmat","0.1");
    model.SetParameter("FluidPrefix","fluid");
    model.SetParameter("BoundaryPrefix","boundary");
    model.SetParameter("SolidPrefix","solid");
    model.SetParameter("VisualizationExt",".vtp");
    model.SetParameter("VisualizationDir","./output");
    model.SetParameter("StepsPerSnapshot","1000");
    model.SetParameter("CurrentStep","0");
    model.SetParameter("StepsPerFrame","100");
    model.SetParameter("CheckpointPrefix","checkpoint");
    model.SetParameter("CheckpointExt",".vtp");
    model.SetParameter("CheckpointDir","./checkpoint");
    model.SetParameter("OutputFormat","binary");
    model.SetParameter("Cg","%f" % (0.4*speedsound));
    model.SetParameter("PlasticityModel","2");
    model.SetParameter("DamageModel","1");
    model.SetParameter("DampingCoef","0.05");
    model.SetParameter("IsImposedDisplacement","false");
    model.SetParameter("Impdx","");
    model.SetParameter("Impdy","");
    model.SetParameter("Impdz","");
    model.SetParameter("IsFloatingObjectRotation","false");
    model.SetParameter("FloatingObjectAppliedFx","false");
    model.SetParameter("FloatingObjectAppliedFy","false");
    model.SetParameter("FloatingObjectAppliedFz","false");
    model.SetParameter("FloatingObjectAppliedForceRampTime","1");
    model.SetParameter("IsFloatingObjectMotionX","false");
    model.SetParameter("IsFloatingObjectMotionY","false");
    model.SetParameter("IsFloatingObjectMotionZ","false");
    model.SetParameter("Movfx","");
    model.SetParameter("Movfy","");
    model.SetParameter("Movfz","");
    model.SetParameter("Movsxx","");
    model.SetParameter("Movsxy","");
    model.SetParameter("Movsyy","");
    model.SetParameter("Movsyz","");
    model.SetParameter("Movsxz","");
    model.SetParameter("Movszz","");
    model.SetParameter("BoundariesRampTime","1");
    model.SetParameter("Cracksxx","");
    model.SetParameter("Cracksxy","");
    model.SetParameter("Cracksyy","");
    model.SetParameter("Cracksyz","");
    model.SetParameter("Cracksxz","");
    model.SetParameter("Crackszz","");
    model.SetParameter("CrackLength","");
    model.SetParameter("CrackThickness","");
    model.SetParameter("CrackX","");
    model.SetParameter("CrackY","");
    model.SetParameter("CrackZ","");
    model.SetParameter("ReverseMovingX","false");
    model.SetParameter("ReverseMovingY","false");
    model.SetParameter("ReverseMovingZ","false");
    model.SetParameter("IsCrack","false");
    model.SetParameter("IsFloatingObject","false");
    model.SetParameter("IsBoundaryForce","false");
    model.SetParameter("BoundaryForceMinLimit","");
    model.SetParameter("BoundaryForceMaxLimit","");
    model.SetParameter("IntegrationScheme","1");
    model.SetParameter("VerletStep","40");