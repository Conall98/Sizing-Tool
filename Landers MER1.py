# -*- coding: utf-8 -*-
"""
Created on Tue May 31 09:14:57 2022

@author: Conall De Paor
"""


#%%
payload_mass=300 #equivalent to ES Mass
transfer_delta_v = 1 #dependant on Body
body_g = 3.3 #dependant on boy
payload_power = 100

solar_panels_specific_power = [1/32, 1/52, 1/34, 1/29] #Table 10.3 SSE: [XMM, AStra, Comets, ISS]
batteries_specific_energy = [1/(34*3600), 1/(54*3600), 1/(100*3600), 1/(90*3600), 1/(150*3600), 1/(250*3600)]
 #%%
def power_ss(payload_mass, payload_power):
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
 #%%
power_ss(300, 500)

#the propellant system mass will depend on both transfer and landing stage