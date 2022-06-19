import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score 
#%%

ML = pd.read_excel(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\DB.xlsx", 
                               sheet_name = "Manned Landers", 
                               index_col = 0)
UL = pd.read_excel(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\DB.xlsx", 
                               sheet_name = "Science Landers", 
                               index_col = 0)
#%%

def plot(x, y, xlabel, ylabel, group):
#    plt.style.use("classic")
    x = x/1000
    y = y/1000
    plt.figure()
    plt.scatter(x, y, color = "black")
    
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)
    R_square = np.round(r2_score(p(x), y), 2)
        
    
    
    plt.title("{0}\n {1} and {2}.".format(group, xlabel, ylabel), fontsize = "x-large")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    smooth = np.linspace(min(x), max(x), 100)
    
    plt.plot([], [], ' ', label="R_squared: {}".format(R_square))
    
    plt.plot(smooth,p(smooth),"--", color = "black")    
    plt.legend(["R_squared: {}".format(R_square), "trendline", "examples" ], framealpha =1)
    plt.grid()

#    n = ML.index.values.tolist()
#    for i, txt in enumerate(n):
#       plt.annotate(txt, (x[i]+0.5, y[i]+0.5))
#%%
#
plot(UL["mass"][:-3], UL["dry mass"][:-3], "Wet mass (t)", "Dry mass(t)", "UL")
plot(UL["mass"][:-5], UL["payload"][:-5], "Wet mass(t)", "Payload(t)", "UL")
plot(UL["propellent"][:-3], UL["dry mass"][:-3], "Mass(t)", "Dry mass(t)", "UL")

plot(ML["mass"][:-3], ML["dry mass"][:-3], "Wet mass(t)", "Dry mass(t)", "ML")
plot(ML["mass"][:-5], ML["payload"][:-5], "Wet mass(t)", "Payload(t)", "ML")
plot(ML["propellent"][:-3], ML["dry mass"][:-3], "Mass(t)", "Dry mass(t)", "ML")



    