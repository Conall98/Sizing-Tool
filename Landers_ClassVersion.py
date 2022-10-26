# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:23:54 2022

@author: Conall De Paor
"""

from pprint import pprint
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score 
#%% 
def get_landers():
    ALL = pd.read_excel(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\DB.xlsx", 
                        sheet_name = "Landers", index_col = 0)
    #  
    small_pm = []
    small_tm = []
    medium_pm = []
    medium_tm = []
    large_pm = []  
    large_tm = []  
    
    j = 0
    k = 0                      
    l = 0
    
    for i in range(0,len(ALL["bloc payload"])):
        if 1 < ALL.iloc[i,4] < 2000:
            small_pm.append((ALL.iloc[i, 4]))
            small_tm.append((ALL.iloc[i, 2]))
            small = np.array([small_tm,small_pm]).T
            
        if 2000 < ALL.iloc[i,4] < 5000:
            medium_pm.append(ALL.iloc[i, 4])
            medium_tm.append(ALL.iloc[i, 2])
            medium = np.array([medium_tm, medium_pm]).T
            
        if 5000 < ALL.iloc[i,4]:
            large_pm.append(ALL.iloc[i, 4])
            large_tm.append(ALL.iloc[i, 2])
            large = np.array([large_tm, large_pm]).T
            
    
    return small, medium, large, ALL
#%% 
def regression(x, y): #(bloc_payload, total_mass)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    return p
#%%
def SizingRuleFinder(small, medium, large):
    p_small = regression(small[:, 1], small[:, 0])
    a_small = np.round(p_small[1], 5)
    b_small = np.round(p_small[0], 5)
    
    p_medium = regression(medium[:, 1], medium[:, 0])
    a_medium = np.round(p_medium[1], 5)
    b_medium = np.round(p_medium[0], 5)
    
    p_large = regression(large[:, 1], large[:, 0])
    a_large = np.round(p_large[1], 5)
    b_large = np.round(p_large[0], 5)

    sizing_coefficients = np.array([[a_small, b_small],[a_medium, b_medium],[a_large, b_large]])
    return sizing_coefficients

#%%
small, medium, large, ALL = get_landers()
sizing_coeffs = SizingRuleFinder(small, medium, large)
 

#%%

class Lander_class():
    def __init__(self, payload_mass):
        self.payload_mass = payload_mass
        if payload_mass < 2000:
            self.total_mass = sizing_coeffs[0,0]*payload_mass + sizing_coeffs[0,1]
        elif 2000 < payload_mass < 5000:
            self.total_mass = sizing_coeffs[1,0]*payload_mass + sizing_coeffs[1,1]
        elif payload_mass > 5000:
            self.total_mass = sizing_coeffs[2,0]*payload_mass + sizing_coeffs[2,1]
        
#%% Test
## A DataClass object
Lander = Lander_class(2001)

#%% Build

#%%
print(Lander.total_mass)
    

















