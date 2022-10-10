# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:12:09 2022

@author: Conall De Paor
"""

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score 
#%%  Getting and classifying the landers

class Lander:
    def __init__(self,total_mass,payload_mass = None):
        self.total_mass = total_mass
        self.payload_mass = payload_mass
        
    def give_name(self,name):
        self.name = name
        print(f"hello, my name is {name}!")
        return self
        
        
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
        
#%% Finding the Regressions Sizing Rules
def regression(x, y): #(bloc_payload, total_mass)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    return p
#%% Statistical Sizing
def Rough_Lander_Sizing(bloc_payload):
    if bloc_payload < 2000:
        lander_class = small_landers
        print("small")
    elif 2000< bloc_payload < 5000:
        lander_class = medium_landers
        print("medium")
    elif 5000 < bloc_payload:
        lander_class = large_landers
        print("large")
    p = regression(lander_class[:, 1], lander_class[:, 0])
    a = np.round(p[0], 5)
    b = np.round(p[1], 5)
    x = bloc_payload
    total_mass = a*x+b
    
    print("{0}bloc_payload+{1}".format(np.round(p[1], 5), 
                                  np.round(p[0], 5)))
    
    return total_mass

if __name__ == "__main__":
    #%% Test
    total_mass = Rough_Lander_Sizing(5001)
    #%% 
        
    small_landers, medium_landers, large_landers, ALL = get_landers()
    
    #%%
    ALL.iloc[:,2]
    add = np.array([ALL.iloc[:,2], ALL.iloc[:,4]]).T
    #%%
    lander1 = Lander(1000, 12)
    lander2 = Lander(21, 12)
    landers = [lander1, lander2]
    for i, lander in enumerate(landers):
        print("weigth lander {0:d} = {1:d}".format(i, lander.total_mass))   
        
    lander1.give_name("Paul")












