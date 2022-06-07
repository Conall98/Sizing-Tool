# -*- coding: utf-8 -*-
"""
Created on Tue May 31 09:14:57 2022

@author: Conall De Paor
"""
import numpy as np
import matplotlib.pyplot as plt
#%%
payload_mass=300 #equivalent to ES Mass
payload_power = 100

#%% Some Power subsystem parameters
solar_panels_specific_power = [1/32, 1/52, 1/34, 1/29] #Table 10.3 SSE: [XMM, AStra, Comets, ISS]
batteries_specific_energy = [1/(34*3600), 1/(54*3600), 1/(100*3600), 1/(90*3600), 1/(150*3600), 1/(250*3600)]
 #%%
def power_ss(payload_power):
    if payload_power < 100:
        payload_power_share = 0.35
    elif payload_power > 100 & payload_power<500:
        payload_power_share = 0.2
    elif payload_power > 500:
        payload_power_share = 0.16
    total_power = payload_power/payload_power_share
    
    #Sizing case for power generation is total power+battery charge requirement
    #sizing case for the batteries if eclipse in LEO    
    LEO_period = 5400
    sunlight_time = 3360
    eclipse_time = LEO_period - sunlight_time
    power_gen_req = total_power*(LEO_period/sunlight_time)

    power_storage_req = total_power*eclipse_time
    
    power_gen_mass = power_gen_req*solar_panels_specific_power[1]
    power_storage_mass = power_storage_req*batteries_specific_energy[1]
    
    power_ss_mass = power_gen_mass + power_storage_mass
    
    return power_ss_mass
 #%% testing the power subsystem function
mass = power_ss(500)
#%%
#the propellant system mass will depend on both transfer and landing stage
# assume trajectory from EML-1 to lunar surface
def propulsion_ss(payload_mass):
    dV = 2500 # required dV for EML-1 to lunar surface. see the chart
    Isp = 300 #assuming chemical bipropellent
    exhaust_velocity = 300*9.81
    total_mass = payload_mass/0.1
    lander_mass = total_mass-payload_mass
    structural_ratio = -(payload_mass*(1-np.exp((dV)/(exhaust_velocity)))/lander_mass) + ((1)/(lander_mass))
    fuel_mass = lander_mass*(1-structural_ratio)
    return fuel_mass #will return both structural mass and fuel mass
#%% testing the propulsion subsystem
print(propulsion_ss(300))
x = np.linspace(50, 550, 101)
y = np.zeros(101)
for i in range(0,101):
    y[i] = propulsion_ss(x[i])
plt.figure()
plt.plot(x, y)
plt.xlabel("payload mass kg")
plt.ylabel("fuel mass kg")
    
z = y/x
# I think it's wring because there's a linear relationship with payload mass and fuel mass












