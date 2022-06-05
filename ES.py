# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:27:25 2022

@author: andre
"""
import numpy as np
#                            struct thermal mechanisms comms OBC/DHS  GNC   robotics  power  harness payload
MassPercentages = np.array([[0.0776, 0.0296, 0.0695, 0.1043, 0.0465, 0.0158, 0.2360, 0.2555, 0.0476, 0.1176],  #MarsFast
                            [0.0862, 0.1585, 0.1220, 0.0305, 0.0107, 0.0790, 0.2864, 0.0837, 0.0711, 0.0719],  
                            [0.1286, 0.1143, 0.1102, 0.0642, 0.1431, 0.0176, 0.0285, 0.1650, 0.1220, 0.1065], 
                            [0.1912, 0.1340, 0.0605, 0.0453, 0.1194, 0.0206, 0.1256, 0.1024, 0.1128, 0.0883], 
                            [0.0887, 0.1269, 0.1496, 0.0662, 0.1149, 0.0863, 0.1321, 0.0857, 0.1414, 0.0082],  
                            [0.1728, 0.1732, 0.1483, 0.0305, 0.0750, 0.0832, 0.1853, 0.0247, 0.0975, 0.0095]]) 


class wheeledRover:
    def __init__(self, name, nWheels, planet, SSMassDistribution, SSEnergyDistribution):
        self.name = name
        self.nWheels = nWheels
        self.planet = planet
        self.SSMassDistribution = SSMassDistribution
        self.SSEnergyDistribution = SSEnergyDistribution
        

MarsFASTMasses = [0.0776, 0.0296, 0.0695, 0.1043, 0.0465, 0.0158, 0.2360, 0.2555, 0.0476, 0.1176]  #REAL 
MarsFASTPowers = [0.0000, 0.0698, 0.4496, 0.0329, 0.2741, 0.0360, 0.0000, 0.0768, 0.0000, 0.0658]  #REAL
MarsFAST = wheeledRover("MarsFAST", 6, "Mars", MarsFASTMasses, MarsFASTPowers)

SojournerMasses = [0.1286, 0.1143, 0.1102, 0.0642, 0.1431, 0.0176, 0.0285, 0.1650, 0.1220, 0.1065]
SojournerPowers = [0.1912, 0.134 , 0.0605, 0.0453, 0.1194, 0.0206, 0.1256, 0.1024, 0.1128, 0.0883]
Sojourner = wheeledRover("Sojourner", 6, "Mars", SojournerMasses, SojournerPowers)

LMRSHCMasses = [0.1286, 0.1143, 0.1102, 0.0642, 0.1431, 0.0176, 0.0285, 0.1650, 0.1220, 0.1065]
LMRSHCPowers = [0.1912, 0.134 , 0.0605, 0.0453, 0.1194, 0.0206, 0.1256, 0.1024, 0.1128, 0.0883]
LMRSHC = wheeledRover("LMRSHC", 8, "Mars", LMRSHCMasses, LMRSHCPowers)

listOfWheeledRovers = [MarsFAST, Sojourner]
#for rover in listOfWheeledRovers:
    #averageMassBugdets = sum of mass budgets / len(listOfWheeledRovers)
    #averagePowerBugdets = sum of power budgets / len(listOfWheeledRovers)


class trackedRover:
    def __init__(self, name, nWheels, planet, SSMassDistribution, SSEnergyDistribution):
        self.name = name
        self.nWheels = nWheels
        self.planet = planet
        self.SSMassDistribution = SSMassDistribution
        self.SSEnergyDistribution = SSEnergyDistribution

Tracked1Masses = [0.1286, 0.1143, 0.1102, 0.0642, 0.1431, 0.0176, 0.0285, 0.1650, 0.1220, 0.1065]
Tracked1Powers = [0.1912, 0.134 , 0.0605, 0.0453, 0.1194, 0.0206, 0.1256, 0.1024, 0.1128, 0.0883]
Tracked1 = trackedRover("Tracked1", 1, "Mars", Tracked1Masses, Tracked1Powers)

Tracked2Masses = [0.1286, 0.1143, 0.1102, 0.0642, 0.1431, 0.0176, 0.0285, 0.1650, 0.1220, 0.1065]
Tracked2Powers = [0.1912, 0.134 , 0.0605, 0.0453, 0.1194, 0.0206, 0.1256, 0.1024, 0.1128, 0.0883]
Tracked2 = trackedRover("Tracked2", 1, "Mars", Tracked2Masses, Tracked2Powers)

listOfTrackedRovers = [Tracked1, Tracked2]

#for rover in listOfWheeledRovers:
    #averageMassBugdets = sum of mass budgets / len(listOfWheeledRovers)
    #averagePowerBugdets = sum of power budgets / len(listOfWheeledRovers)



class leggedRover:
    def __init__(self, name, tip, planet, SSMassDistribution, SSEnergyDistribution):
        self.name = name
        self.tip = tip #(leg0, leg1, leg2, wheels, skis, hybrid)
        self.planet = planet
        self.SSMassDistribution = SSMassDistribution
        self.SSEnergyDistribution = SSEnergyDistribution

ATHLETEMasses = [0.1286, 0.1143, 0.1102, 0.0642, 0.1431, 0.0176, 0.0285, 0.1650, 0.1220, 0.1065]
ATHLETEPowers = [0.1912, 0.1340, 0.0605, 0.0453, 0.1194, 0.0206, 0.1256, 0.1024, 0.1128, 0.0883]
ATHLETE = wheeledRover("ATHLETE", "wheels", "Mars", ATHLETEMasses, ATHLETEPowers)

PropMMasses = [0.1286, 0.1143, 0.1102, 0.0642, 0.1431, 0.0176, 0.0285, 0.1650, 0.1220, 0.1065]
PropMPowers = [0.1912, 0.1340, 0.0605, 0.0453, 0.1194, 0.0206, 0.1256, 0.1024, 0.1128, 0.0883]
PropM = wheeledRover("PropM", "skis", "Mars", PropMMasses, PropMPowers)

listOfLeggedRovers = [ATHLETE, PropM]
#for rover in listOfWheeledRovers:
    #averageMassBugdets = sum of mass budgets / len(listOfWheeledRovers)
    #averagePowerBugdets = sum of power budgets / len(listOfWheeledRovers)


class Hopper:
    def __init__(self, name, propulsionType, planet, SSMassDistribution, SSEnergyDistribution):
        self.name = name
        self.propulsionType = propulsionType  # (thrust, mechanical, hybrid)
        self.planet = planet
        self.SSMassDistribution = SSMassDistribution
        self.SSEnergyDistribution = SSEnergyDistribution

class Slider:
    def __init__(self, name, nWheels, planet, SSMassDistribution, SSEnergyDistribution):
        self.name = name
        self.nWheels = nWheels
        self.planet = planet
        self.SSMassDistribution = SSMassDistribution
        self.SSEnergyDistribution = SSEnergyDistribution

class Aerial:
    def __init__(self, name, liftMethod, planet, SSMassDistribution, SSEnergyDistribution):
        self.name = name
        self.liftMethod = liftMethod # (fixed wing, rotary wing, buoyancy/balloon type)
        self.planet = planet
        self.SSMassDistribution = SSMassDistribution
        self.SSEnergyDistribution = SSEnergyDistribution


# make average of values above


# MAKE TEXT FILE THAT POTH PY'S TALK TO
# THIS ONE WRITES, THE OTHER PY READS IT 

# structure
# comms
# data/OBC
# GNC/AOCS
# robotics
# power
# harness
# instruments/payload
# mobility