# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:00:29 2022

@author: andre
"""

import numpy as np
import pandas as pd



PayloadMass = input("Estimated Payload Mass (kg): ")
PayloadMass = float(PayloadMass)
PayloadPower = input("Estimated Payload Power (W): ")
PayloadPower = float(PayloadPower)
MissionDuration = input("Expected mission duration (days): ") 
MissionDuration = float(MissionDuration)
Body = input("To what planetary body will the mission go to? \n - Moon \n - Mars \n ")

excel = pd.read_excel (r'C:\Users\andre\Desktop\2º Semestre\(RESEARCH PROJECT)\db.xlsx')
db = excel.to_numpy()

TotalMass = 1.2242 * PayloadMass + 527.67

def PowerSubsystem(PayloadMass, PayloadPower, MissionDuration, Body):

    i = 0 
    sum = 0
    for line in db:   
        if line[1] == "Hopper":
            if line[4] != 0.0:   
                sum = sum + line[4]
                i = i + 1
    
    TotalMass = 1.2242 * PayloadMass + 527.67  # FROM NOTION, GET PAPER NAME 
    
    if PayloadPower < 100:
        payloadPowerFraction = 0.35
    elif (PayloadPower >= 100) & (PayloadPower <= 500):
        payloadPowerFraction = 0.2
    elif PayloadPower > 500:
        payloadPowerFraction = 0.16
        
    TotalPower = float(PayloadPower)/payloadPowerFraction
    
        
    print("\nThe total rover mass will be of " + str(round(TotalMass,3)) + " kg.")
    print("The total rover power will be of " + str(round(TotalPower,3)) + " W. \n")
    if TotalPower > 10000:
        print("\nThe total power need will probably exceed 10 kW, consider AC current distribution, both sine wave and square wave, at several hundred volts. (SMAD Chapter 10.4.6)\n\n")
    
    
    if Body == "Moon":
        solarIrradiance = 1367.6 #Wikipedia
    elif Body == "Mars":
        solarIrradiance = 591  #Wikipedia
    PanelPowerDensity = 30 #W/kg average found in 10.4.6 of SMAD, range 14-47 W/Kg at EOL
    solarPanelEfficiency = 0.10 # Standard Values go from 5%-15%
    
    areaSolarPanels = TotalPower / (solarPanelEfficiency * solarIrradiance)
    mSolarPanels = TotalPower * (1367.6/solarIrradiance)/PanelPowerDensity
     
    print("Area of Solar Panels is " + str(round(areaSolarPanels, 3)) + " m2 \n")
    print("Mass of Solar Panels is " + str(round(mSolarPanels, 3)) + " kg")
    
    if Body == "Moon":
        if MissionDuration > 14:
            #Take into account the dark time for recharging
            upTime = 14 * 24
        else: upTime = MissionDuration * 24
    elif Body == "Mars":
        upTime = MissionDuration * 24
    
    
    batteryEnergyDensity = 140 # W.h/kg for a Li-Ion battery SMAD (for NiCd use 35-45)
    batteryCapacity = TotalPower * upTime * 0.15 # THIS 0.15 IS VERY EXPERIMENTAL AND MUST BE EXPLAINED WITH JASMINE
    mBattery = batteryCapacity/batteryEnergyDensity
    
    print("Mass of the Batteries is " + str(round(mBattery, 3)) + " kg")
    
    mPowerControlUnit = 0.02 * TotalPower  #Table 10-27 SMAD
    mRegulator = 0.025 * TotalPower  #Table 10-27 SMAD
    mWiring = 0.01 * TotalMass    # 0.01 - 0.04 Table 10-27 SMAD 
    
    print("Mass of the Power Control Unit is " + str(round(mPowerControlUnit, 3)) + " kg")
    print("Mass of the Regulator is " + str(round(mRegulator, 3)) + " kg")
    print("Mass of the Wiring is " + str(round(mWiring, 3)) + " kg \n")
    
    
    mPowerSS = mSolarPanels + mBattery + mPowerControlUnit + mRegulator + mWiring
    
    print("Mass of the Power SS will be " + str(round(mPowerSS, 3)) + " kg, representing " + str(round(100*mPowerSS/TotalMass,4)) + "% of the total mass." )
    
    PowerSSMasses = [mPowerSS, mSolarPanels, mBattery, mPowerControlUnit, mRegulator, mWiring]
    
    return PowerSSMasses

def MobilitySubsystem(PayloadMass, PayloadPower, MissionDuration, Body):
    
    s = 1
    T = 2
    
    mEngine = 0.1 * s**2/TotalMass * pow(T, 2/3)
    mTank = 2/3 * pow(PayloadMass,(2/3))   
    
    mMobilitySS = mEngine + mTank
    
    MobilitySSMasses = [mMobilitySS]
    #NO FUEL IS CONSIDERED (DRY MASS)

    return MobilitySSMasses

def StructuresSubsystem(PayloadMass, PayloadPower, MissionDuration, Body):
    #PLACEHOLDER FOR NOW
    mStructureSS = 0.15 * TotalMass
    
    StructuresSSMasses = [mStructureSS]
    
    return StructuresSSMasses

power = PowerSubsystem(PayloadMass, PayloadPower, MissionDuration, Body)
print(power)
mobility = MobilitySubsystem(PayloadMass, PayloadPower, MissionDuration, Body)
print(mobility) 
structures = StructuresSubsystem(PayloadMass, PayloadPower, MissionDuration, Body)
print(structures) 


