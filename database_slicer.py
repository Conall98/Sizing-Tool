import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score 
#%% Database you want to plot stuff from

ML = pd.read_excel(r"DB.xlsx", sheet_name = "Manned Landers", index_col = 0)
                               
                              
UL = pd.read_excel(r"DB.xlsx", sheet_name = "Science Landers",index_col = 0)
                               
                               
#%% plot function

def plot(x, y, xlabel, ylabel, group):
#    plt.style.use("classic")
    x = x/1000
    y = y/1000
    plt.figure()
    plt.scatter(x, y, color = "black")
    # making the trendline
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)
    R_square = np.round(r2_score(p(x), y), 2)
        
    
    #Title and axes
    plt.title("{0}\n {1} and {2}.".format(group, xlabel, ylabel), fontsize = "x-large")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #making points to draw the line for the polynomial of best fit.
    smooth = np.linspace(min(x), max(x), 100)
    #blank dot so that R squared will appear in the legend
    plt.plot([], [], ' ', label="R_squared: {}".format(R_square))
    
    plt.plot(smooth,p(smooth),"--", color = "black")    
    plt.legend(["R_squared: {}".format(R_square), "trendline", "examples" ], framealpha =1)
    plt.grid()

#%%
#Plot what you want
plot(UL["mass"][:-3], UL["dry mass"][:-3], "Wet mass (t)", "Dry mass(t)", "UL")
plot(UL["mass"][:-5], UL["payload"][:-5], "Wet mass(t)", "Payload(t)", "UL")
plot(UL["propellent"][:-3], UL["dry mass"][:-3], "Mass(t)", "Dry mass(t)", "UL")

plot(ML["mass"][:-3], ML["dry mass"][:-3], "Wet mass(t)", "Dry mass(t)", "ML")
plot(ML["mass"][:-5], ML["payload"][:-5], "Wet mass(t)", "Payload(t)", "ML")
plot(ML["propellent"][:-3], ML["dry mass"][:-3], "Mass(t)", "Dry mass(t)", "ML")



    