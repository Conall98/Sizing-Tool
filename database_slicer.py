import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score 
#%% Database you want to plot stuff from

ALL = pd.read_excel(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\DB.xlsx", sheet_name = "export sheet", index_col = 0)
#  
small = []
medium = []
large = []  
j = 0
k = 0                      
l = 0

for i in range(0,len(ALL["bloc payload"])):
    if 1 < ALL.iloc[i,6] < 2000:
        j = j+1
        small = (ALL.iloc[2:i+1,:])
    if 2000 < ALL.iloc[i,6] < 5000:
        print(j)
        k = k+1
        medium = (ALL.iloc[j+2-len(ALL):i+1, :])
    if 5000 < ALL.iloc[i,6]:
        print(k)
        large = (ALL.iloc[j+k+2-len(ALL):i+1, :])
#    
#UL = pd.read_excel(r"DB.xlsx", sheet_name = "Science Landers",index_col = 0)
#                               
                               
#%% plot function

def plot(x, y, xlabel, ylabel, group):
#    plt.style.use("classic")
    x = x/1000
    y = y/1000
    plt.figure()
    plt.scatter(x, y, color = "tab:blue")
    # making the trendline
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    R_square = np.round(r2_score(p(x), y), 2)
    eqn_strng = "{0}{2}+{1}".format(np.round(p[1], 5), 
                                  np.round(p[0], 5),
                                  xlabel)    
    
    #Title and axes
    plt.title("{0}\n {1} and {2}.".format(group, xlabel, ylabel), fontsize = "x-large")
    plt.xlabel(xlabel +" [t]", fontsize = 14)
    plt.ylabel(ylabel +" [t]", fontsize = 14)
    #making points to draw the line for the polynomial of best fit.
    smooth = np.linspace(min(x), max(x), 100)
    #blank dot so that R squared will appear in the legend
    plt.plot([], [], ' ', label="equation: {}".format(eqn_strng))
    plt.plot([], [], ' ', label="R_squared: {}".format(R_square))
    
    plt.plot(smooth,p(smooth),"--", color = "tab:blue")    
    plt.legend(["R\u00b2 = {}".format(R_square), 
                "{1}={0}".format(eqn_strng, ylabel), 
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
    plt.savefig(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\Results\{0}_{1}_{2}".format(group, xlabel, ylabel))

#%%
#Plot what you want
plot(small["mass"].values, small["dry mass"].values, "$m_0$", "$m_f$", "small landers")
plot(small["bloc payload"].values, small["mass"].values, "$m_p$", "$m_0$", "small landers")

plot(medium["mass"].values, medium["dry mass"].values, "$m_0$", "$m_f$", "medium landers")
plot(medium["bloc payload"].values, medium["mass"].values, "$m_p$", "$m_0$", "medium landers")

plot(large["mass"].values, large["dry mass"].values, "$m_0$", "$m_f$", "Large Landers")
plot(large["bloc payload"].values, large["mass"].values,  "$m_p$", "$m_0$", "Large Landers")
#

#plot(ALL[""], ALL["bloc payload"], "Wet mass (t)", "Dry mass(t)", "ALL")
#plot(UL["mass"][:-6], UL["payload"][:-6], "Wet mass(t)", "Payload(t)", "UL")
#plot(UL["propellent"], UL["dry mass"], "Propellent(t)", "Dry mass(t)", "UL")
#
#plot(ML["mass"], ML["dry mass"], "Wet mass(t)", "Dry mass(t)", "ML")
#plot(ML["mass"], ML["payload"], "Wet mass(t)", "Payload(t)", "ML")
#plot(ML["propellent"], ML["dry mass"], "Propellent(t)", "Dry mass(t)", "ML")



    