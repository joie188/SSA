# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import time

#%%

data = pd.read_csv("AstroYWeek1DataSet.csv")


data = pd.read_csv("AstroYWeek2DataSeT.csv")

def gather_data(file, pattern_type):
    data = pd.read_csv(file)
    current_id = 0
    sat_dict = {}
    epoch_time = []
    
    for i in range(len(data)):
        row = data.iloc[i]
        if pattern_type == 1:
            pattern = '%Y-%m-%d %H:%M:%S'
        else:
            pattern = '%m/%d/%Y %H:%M'
        norm_time = int(time.mktime(time.strptime(row["EPOCH"], pattern)))
        epoch_time.append(norm_time)
    
    data['TIME'] = epoch_time

    for i in range(len(data)):
        row = data.iloc[i]
        if row["NORAD_CAT_ID"] != current_id:
            current_id = row['NORAD_CAT_ID']
            sat_dict[current_id] = data.loc[data.NORAD_CAT_ID == current_id]
            
    return sat_dict

#%%

sat_list = [9191, 11682, 30206, 79815]
color_list = ['red', 'green', 'blue' 'orange']

attribute_list = ["MEAN_MOTION",
                  "ECCENTRICITY",
                  "INCLINATION",
                  "RA_OF_ASC_NODE",
                  "ARG_OF_PERICENTER",
                  "MEAN_ANOMALY",
                  "SEMIMAJOR_AXIS",
                  "PERIOD",
                  "APOGEE",
                  "PERIGEE"]

plt.close()

plt.subplot(5,2,1)
plt.tight_layout()

mlt.rcParams.update({'font.size': 18})
for i,num in sat_list:
    plt.plot(sat_list[num].TIME, sat_list[num][attribute_list[0]], color=color_list[i], label=str(num))
    plt.title(attribute_list[0].lower())
    plt.legend(loc="upper left")


for i in range(2,11):
    plt.subplot(5,2,i)
    for c,num in sat_list:
        plt.plot(sat_list[num].TIME, sat_list[num][attribute_list[0]], color=color_list[c])
        plt.title(attribute_list[i-1].lower())


plt.show()



     
#
#from win32api import GetSystemMetrics
#import comtypes
#
#from comtypes.client import CreateObject
#
#uiApplication = CreateObject('STK11.Application')
#uiApplication.Visible = True
#root=uiApplication.personality2
#
#root.LoadScenario(r"C:\\Users\\Luke de Castro\\Documents\\STK 11 (x64)\\MainChallenge")
#sc = root.CurrentScenario
#sc2 = sc.QueryInterface(STKObjects.IAgScenario)
#
#sat = sc.Children.New(STKObjects.eSatellite, '74415')
#sat2 = sat.QueryInterface(STKObjects.IAgSatellite)
#

#from win32api import GetSystemMetrics
#import comtypes
#
#from comtypes.client import CreateObject
#
#uiApplication = CreateObject('STK11.Application')
#uiApplication.Visible = True
#root=uiApplication.personality2
#
#
#root.LoadScenario(r"C:\Users\Luke de Castro\Documents\STK 11 (x64)\MainChallenge\MainChallenge.sc")
#sc = root.CurrentScenario
#sc2 = sc.QueryInterface(STKObjects.IAgScenario)
#
#sat = sc.Children.New(STKObjects.eSatellite, '74415')
#
#sat2 = sat.QueryInterface(STKObjects.IAgSatellite) 


    
#from win32api import GetSystemMetrics
#import comtypes

#from comtypes.client import CreateObject

#uiApplication = CreateObject('STK11.Application')
#""" uiApplication.Visible = True
#root=uiApplication.personality2
#
##root.LoadScenario(r"C:\\Users\\Luke de Castro\\Documents\\STK 11 (x64)\\MainChallenge")
#sc = root.CurrentScenario
#sc2 = sc.QueryInterface(STKObjects.IAgScenario)
#
#sat = sc.Children.New(STKObjects.eSatellite, '74415')
##sat2 = sat.QueryInterface(STKObjects.IAgSatellite) """

