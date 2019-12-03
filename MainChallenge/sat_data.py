# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import time

sat_dict = {}

data = pd.read_csv("AstroYWeek1DataSet.csv")
current_id = 0
    
epoch_time = []
for i in range(len(data)):
    row = data.iloc[i]
    #pattern = '%Y-%m-%d %H:%M:%S'
    pattern = '%m/%d/%Y %H:%M'
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
        
        
        
sat_09191 = sat_dict[9191]
sat_11682 = sat_dict[11682]
sat_30206 = sat_dict[30206]
sat_79815 = sat_dict[79815]

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
for num in sat_list:
plt.plot(sat_09191.TIME, sat_09191[attribute_list[0]], color="red", label="09191")
plt.plot(sat_11682.TIME, sat_11682[attribute_list[0]], color="blue", label="11682")
plt.plot(sat_30206.TIME, sat_30206[attribute_list[0]], color='green', label="30206")
plt.plot(sat_79815.TIME, sat_79815[attribute_list[0]], color="orange", label="79815")
plt.title(attribute_list[0].lower())
plt.legend(loc="upper left")


for i in range(2,11):
    plt.subplot(5,2,i)
    plt.plot(sat_09191.TIME, sat_09191[attribute_list[i-1]], color="red")
    plt.plot(sat_11682.TIME, sat_11682[attribute_list[i-1]], color="blue")
    plt.plot(sat_30206.TIME, sat_30206[attribute_list[i-1]], color="green")
    plt.plot(sat_79815.TIME, sat_79815[attribute_list[i-1]], color="orange")
    plt.title(attribute_list[i-1].lower())
    

plt.show()

    
#from win32api import GetSystemMetrics
#import comtypes

#from comtypes.client import CreateObject

#uiApplication = CreateObject('STK11.Application')
""" uiApplication.Visible = True
root=uiApplication.personality2

#root.LoadScenario(r"C:\\Users\\Luke de Castro\\Documents\\STK 11 (x64)\\MainChallenge")
sc = root.CurrentScenario
sc2 = sc.QueryInterface(STKObjects.IAgScenario)

sat = sc.Children.New(STKObjects.eSatellite, '74415')
#sat2 = sat.QueryInterface(STKObjects.IAgSatellite) """
