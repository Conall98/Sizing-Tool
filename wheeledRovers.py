# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 18:24:27 2022

@author: andre
"""

import numpy as np
import pandas as pd

excel = pd.read_excel (r'C:\Users\andre\Desktop\2º Semestre\(RESEARCH PROJECT)\db.xlsx')
db = excel.to_numpy()


PayloadMass = input("Estimated Payload Mass (kg): ")
PayloadMass = float(PayloadMass)
PayloadPower = input("Estimated Payload Power (W): ")
MissionDuration = input("Expected mission duration (days): ") 
MissionDuration = float(MissionDuration)
Body = input("To what planetary body will the mission go to? \n - Moon \n - Mars \n ")
    
i = 0 
sum = 0
for line in db:   
    if line[1] == "Wheeled Rover":
        if line[4] != 0.0:   
            sum = sum + line[4]
            i = i + 1

payloadMassFraction = sum/i
TotalMass = float(PayloadMass)/(payloadMassFraction/100)

if float(PayloadPower) < 100:
    payloadPowerFraction = 0.35
elif float(PayloadPower) > 100 & float(PayloadPower)<500:
    payloadPowerFraction = 0.2
elif float(PayloadPower) > 500:
    payloadPowerFraction = 0.16
    
TotalPower = float(PayloadPower)/payloadPowerFraction

    
print("The total rover mass will be of " + str(TotalMass) + "kg.")


if Body == "Moon":
    solarIrradiance = 1367.6 #Wikipedia
elif Body == "Mars":
    solarIrradiance = 591  #Wikipedia
PanelPowerDensity = 25 #W/kg average found in 10.4.6 of SMAD, range 14-47 W/Kg at EOL
solarPanelEfficiency = 0.12 # Standard Values go from 5%-15%

areaSolarPanels = TotalPower / (solarPanelEfficiency * solarIrradiance)
mPowerSolarPanels = TotalPower/PanelPowerDensity

print("Area of Solar Panels is " + str(round(areaSolarPanels, 3)) + " m2")
print("Mass of Solar Panels is " + str(round(mPowerSolarPanels, 3)) + " kg")

if Body == "Moon":
    if MissionDuration > 14:
        #Take into account the dark time for recharging
        upTime = 14 * 24
    else: upTime = MissionDuration * 24
elif Body == "Mars":
    upTime = MissionDuration * 24


batteryEnergyDensity = 140 # W.h/kg for a Li-Ion battery SMAD
batteryCapacity = TotalPower * upTime * 0.15 # THIS 0.15 IS VERY EXPERIMENTAL AND MUST BE CONFIRMED WITH JASMINE
mBattery = batteryCapacity/batteryEnergyDensity

print("Mass of the Batteries is " + str(round(mBattery, 3)) + " kg")

mPowerControlUnit = 0.02 * TotalPower  #Table 10-27 SMAD
mRegulator = 0.025 * TotalPower  #Table 10-27 SMAD
mWiring = 0.025 * TotalMass    # 0.01 - 0.04 Table 10-27 SMAD 


mPowerSS = mPowerSolarPanels + mBattery + mPowerControlUnit + mRegulator + mWiring

print("Mass of the Power SS will be " + str(round(mPowerSS, 3)) + " kg")






