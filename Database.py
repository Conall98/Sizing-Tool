# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 00:44:44 2022

@author: Conall De Paor
"""

class wheeled_rover:
    def __init__(self, mass, power, body, wheels, name):
        self.mass = mass
        self.power = power
        self.body = body
        self.wheels = wheels
        self.name = name
        

        
Soujourner =    wheeled_rover(10.6, 1, "Mars", 6, "Soujourner")
Spirit =        wheeled_rover(185, 1, "Mars", 6, "Spirit")
Opportunity =   wheeled_rover(185, 1, "Mars", 6, "Opportunity")
Curiousity =    wheeled_rover(899, 1, "Mars", 6, "Curiousity")
Yutu_1 =        wheeled_rover(140, 1, "Moon", 6, "Yutu_1")
ExoMars =       wheeled_rover(207, 1, "Mars", 6, "ExoMars")
Perseverence =  wheeled_rover(1025, 1, "Mars", 6, "Perseverence")
Pragyan =       wheeled_rover(27, 1, "Moon", 6, "Pragyan")
Yutu_2 =        wheeled_rover(140, 1, "Moon", 6, "Yutu_2")
Lunakhod_1 =    wheeled_rover(756, 1, "Moon", 8, "Lunokhod_1")
Lunakhod_2 =    wheeled_rover(836, 1, "Moon", 8, "Lunokhod_2")
