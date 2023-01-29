import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score 
#%% Database you want to plot stuff from

ALL =    pd.read_excel(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\DB23.xlsx", 
                    sheet_name = "All Landers", index_col = 0)
#  
small =  pd.read_excel(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\DB23.xlsx", 
                    sheet_name = "Small", index_col = 0)
medium = pd.read_excel(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\DB23.xlsx", 
                    sheet_name = "Medium", index_col = 0)
large =  pd.read_excel(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\DB23.xlsx", 
                    sheet_name = "Large (analysis)", index_col = 0)

#                               
                               
#%% plot function


def plot(x, y, xlabel, ylabel, group):
#    plt.style.use("classic")
    x = x
    y = y
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
    plt.show()


"""     n = x.index.tolist()
    for i in range(0, len(n)-1):
        plt.annotate(txt, (x[i], y[i]))
        print(n[i])
    return z """

#    plt.savefig(r"C:\Users\Conall De Paor\Desktop\Supaero\Research Project\Sizing-Tool\Results\{0}_{1}_{2}".format(group, xlabel, ylabel))
#%%
#Ideal curve maker
def mp_Tsky(mdry, mpl, dv, Isp):
    mp = (mpl+mdry)*np.exp((dv)/(Isp*9.81))-(mpl+mdry)
    return mp

def mp_Tsky(mdry, mp, dv, Isp):
    mpl = (mp+mdry)*np.exp((dv)/(Isp*9.81))-(mp+mdry)
    return mpl

def mdry_Tsky(mpl, mp, dv, Isp):
    mdry = (mp+mpl)*np.exp((dv)/(Isp*9.81))-(mp+mpl)
    return mdry

#%%
#Plot what you want
x = small["dry mass"].values
y = small["bloc payload (down)"].values
xlabel = "dry mass"
ylabel = "bloc payload"
group = "small"
plot(x, y, xlabel, ylabel, group) 
#%%
slope = 0.34828
offset = -90.098
y_array = []
x_array = np.linspace(0, 2000, 2000)
y_array = x_array*slope + offset
varoi = np.zeros(len(x_array))
for i in range(0,2000):
    varoi[i] = mp_Tsky(x_array[i], y_array[i], 2250, 311)
plt.figure()
plt.plot(x_array, varoi)
plt.scatter(small["dry mass"].values, small["resultant prop mass"].values)
#%%
