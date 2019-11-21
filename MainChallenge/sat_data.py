# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

sat_dict = {}


data = pd.read_csv("AstroYWeek1DataSet.csv")

data = pd.read_csv("AstroYWeek2DataSeT.csv")

current_id = 0
    
epoch_time = []
for i in range(len(data)):
    row = data.iloc[i]
    pattern = '%Y-%m-%d %H:%M:%S'
    norm_time = int(time.mktime(time.strptime(row["EPOCH"], pattern)))
    epoch_time.append(norm_time)

data['TIME'] = epoch_time

#%%
for i in range(len(data)):
    row = data.iloc[i]
    if row["NORAD_CAT_ID"] != current_id:
        current_id = row['NORAD_CAT_ID']
        sat_dict[current_id] = data.loc[data.NORAD_CAT_ID == current_id]

#%%
sat_74415 = sat_dict[9191]

plt.subplot(5, 2, 1)
plt.plot(sat_74415.TIME, sat_74415.MEAN_MOTION)
plt.title("mean motion")

plt.subplot(5,2,2)
plt.plot(sat_74415.TIME,sat_74415.ECCENTRICITY)
plt.title("eccentricity")

plt.subplot(5,2,3)
plt.plot(sat_74415.TIME,sat_74415.INCLINATION)
plt.title('inclination')

plt.subplot(5,2,4)
plt.plot(sat_74415.TIME,sat_74415.RA_OF_ASC_NODE)
plt.title('ra of asc node')

plt.subplot(5,2,5)
plt.plot(sat_74415.TIME,sat_74415.ARG_OF_PERICENTER)
plt.title('pericenter')

plt.subplot(5,2,6)
plt.plot(sat_74415.TIME,sat_74415.MEAN_ANOMALY)
plt.title('mean anomaly')

plt.subplot(5,2,7)
plt.plot(sat_74415.TIME,sat_74415.SEMIMAJOR_AXIS)
plt.title('semimajor axis')

plt.subplot(5,2,8)
plt.plot(sat_74415.TIME,sat_74415.PERIOD)
plt.title('period')

plt.subplot(5,2,9)
plt.plot(sat_74415.TIME,sat_74415.APOGEE)
plt.title('apogee')

plt.subplot(5,2,10)
plt.plot(sat_74415.TIME,sat_74415.PERIGEE)
plt.title('perigee')

plt.show()

     

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


