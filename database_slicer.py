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
    plt.scatter(x, y, color = "tab:blue")
    # making the trendline
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)
    R_square = np.round(r2_score(p(x), y), 2)
    eqn_strng = "{0}x\u00b2+{1}x+{2}".format(np.round(z[0]*1000), 
                                              np.round(z[1]*1000), 
                                              np.round(z[2]*1000))    
    
    #Title and axes
    plt.title("{0}\n {1} and {2}.".format(group, xlabel, ylabel), fontsize = "x-large")
    plt.xlabel(xlabel, fontsize = 14)
    plt.ylabel(ylabel, fontsize = 14)
    #making points to draw the line for the polynomial of best fit.
    smooth = np.linspace(min(x), max(x), 100)
    #blank dot so that R squared will appear in the legend
    plt.plot([], [], ' ', label="equation: {}".format(eqn_strng))
    plt.plot([], [], ' ', label="R_squared: {}".format(R_square))
    
    plt.plot(smooth,p(smooth),"--", color = "tab:blue")    
    plt.legend(["R\u00b2 = {}".format(R_square), 
                "y={}".format(eqn_strng), 
                "trendline", 
                "examples"], 
                framealpha =1, prop={"size":9.5})
    plt.grid()
    

    
#    return z
#    if datalabels == 1:
#        n = x.index.tolist()
##        for i in range(0, len(n)-1):
##            if n[i][:5] == n[i][:5]:
###                plt.annotate(txt, (x[i], y[i]))
##                print(n[i])
    plt.savefig(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\Results\{0}_{1}_{2}_Annotated".format(group, xlabel, ylabel))

#%%
#Plot what you want
plot(UL["mass"], UL["dry mass"], "Wet mass (t)", "Dry mass(t)", "UL")
plot(UL["mass"][:-6], UL["payload"][:-6], "Wet mass(t)", "Payload(t)", "UL")
plot(UL["propellent"], UL["dry mass"], "Propellent(t)", "Dry mass(t)", "UL")

plot(ML["mass"], ML["dry mass"], "Wet mass(t)", "Dry mass(t)", "ML")
plot(ML["mass"], ML["payload"], "Wet mass(t)", "Payload(t)", "ML")
plot(ML["propellent"], ML["dry mass"], "Propellent(t)", "Dry mass(t)", "ML")



    