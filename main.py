# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:09:45 2022

@author: Conall De Paor
"""

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score 
import Landers as lr
import wheeledRovers as wr
import tkinter as tk
from tkinter import ttk
from tkinter import * 

#%%


#%%
#import tkinter as tk
#from tkinter import ttk
#from tkinter import * 

# this is a function to get the user input from the text input box
#def getInputBoxValue():
#	userInput = tInput.get()
#	return userInput
#
#
## this is the function called when the button is clicked
#def buttonpress(function, *args):
#    value = function(*args)    
#    return value
#
#def btnClickFunction():
#    payload_mass = getInputBoxValue()
#    payload_power = 1000
#    mission_duration = 14
#    body = "Moon"
#    rover_mass = wr.Rover_Mass(payload_mass, payload_power, mission_duration, body)
#    lander_mass = lr.Rough_Lander_Sizing(rover_mass)
#	print('clicked')


#%%
#payload_mass = getInputBoxValue()
payload_mass = 100
payload_power = 1000
mission_duration = 14
body = "Moon"
rover_mass = wr.Rover_Mass(payload_mass, payload_power, mission_duration, body)
lander_mass = lr.Rough_Lander_Sizing(rover_mass)

#%%
print(payload_mass)
print(rover_mass)
print(lander_mass)
#%%


#root = Tk()
#
## This is the section of code which creates the main window
#root.geometry('491x292')
#root.configure(background='#8B8378')
#root.title('Hello, I\'m the main window')
#
#
## This is the section of code which creates a text input box
#tInput=Entry(root)
#tInput.place(x=102, y=97)
#
#
## This is the section of code which creates a button
#Button(root, text='Button text!', bg='#8B8378', font=('arial', 12, 'normal'), 
#       command = btnClickFunction).place(x=142, y=197)
## This is the section of code which creates the a label
#
#Label(root, text="some text", bg='#8B8378', font=('arial', 12, 'normal')).place(x=302, y=137)
#
#
#root.mainloop()


#%%

