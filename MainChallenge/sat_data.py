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

#sat_dict = gather_data("AstroYWeek2DataSeT.csv", 1)
#sat_09191 = sat_dict[9191]
#sat_11682 = sat_dict[11682]
#sat_30206 = sat_dict[30206]
#sat_79815 = sat_dict[79815]
#
#plt.subplot(5, 2, 1)
#plt.plot(sat_09191.TIME, sat_09191.MEAN_MOTION)
#plt.plot(sat_11682.TIME, sat_11682.MEAN_MOTION)
#plt.plot(sat_30206.TIME, sat_30206.MEAN_MOTION)
#plt.plot(sat_79815.TIME, sat_79815.MEAN_MOTION)
#plt.title("mean motion")
#
#plt.subplot(5,2,2)
#plt.plot(sat_09191.TIME,sat_09191.ECCENTRICITY)
#plt.plot(sat_11682.TIME,sat_11682.ECCENTRICITY)
#plt.plot(sat_30206.TIME,sat_30206.ECCENTRICITY)
#plt.plot(sat_79815.TIME,sat_79815.ECCENTRICITY)
#plt.title("eccentricity")
#
#plt.subplot(5,2,3)
#plt.plot(sat_09191.TIME,sat_09191.INCLINATION)
#plt.plot(sat_11682.TIME,sat_11682.INCLINATION)
#plt.plot(sat_30206.TIME,sat_30206.INCLINATION)
#plt.plot(sat_79815.TIME,sat_79815.INCLINATION)
#plt.title('inclination')
#
#plt.subplot(5,2,4)
#plt.plot(sat_09191.TIME,sat_09191.RA_OF_ASC_NODE)
#plt.plot(sat_11682.TIME,sat_11682.RA_OF_ASC_NODE)
#plt.plot(sat_30206.TIME,sat_30206.RA_OF_ASC_NODE)
#plt.plot(sat_79815.TIME,sat_79815.RA_OF_ASC_NODE)
#plt.title('ra of asc node')
#
#plt.subplot(5,2,5)
#plt.plot(sat_09191.TIME,sat_09191.ARG_OF_PERICENTER)
#plt.plot(sat_11682.TIME,sat_11682.ARG_OF_PERICENTER)
#plt.plot(sat_30206.TIME,sat_30206.ARG_OF_PERICENTER)
#plt.plot(sat_79815.TIME,sat_79815.ARG_OF_PERICENTER)
#plt.title('pericenter')
#
#plt.subplot(5,2,6)
#plt.plot(sat_09191.TIME,sat_09191.MEAN_ANOMALY)
#plt.plot(sat_11682.TIME,sat_11682.MEAN_ANOMALY)
#plt.plot(sat_30206.TIME,sat_30206.MEAN_ANOMALY)
#plt.plot(sat_79815.TIME,sat_79815.MEAN_ANOMALY)
#plt.title('mean anomaly')
#
#plt.subplot(5,2,7)
#plt.plot(sat_09191.TIME,sat_09191.SEMIMAJOR_AXIS)
#plt.plot(sat_11682.TIME,sat_11682.SEMIMAJOR_AXIS)
#plt.plot(sat_30206.TIME,sat_30206.SEMIMAJOR_AXIS)
#plt.plot(sat_79815.TIME,sat_79815.SEMIMAJOR_AXIS)
#plt.title('semimajor axis')
#
#plt.subplot(5,2,8)
#plt.plot(sat_09191.TIME,sat_09191.PERIOD)
#plt.plot(sat_11682.TIME,sat_11682.PERIOD)
#plt.plot(sat_30206.TIME,sat_30206.PERIOD)
#plt.plot(sat_79815.TIME,sat_79815.PERIOD)
#plt.title('period')
#
#plt.subplot(5,2,9)
#plt.plot(sat_09191.TIME,sat_09191.APOGEE)
#plt.plot(sat_11682.TIME,sat_11682.APOGEE)
#plt.plot(sat_30206.TIME,sat_30206.APOGEE)
#plt.plot(sat_79815.TIME,sat_79815.APOGEE)
#plt.title('apogee')
#
#plt.subplot(5,2,10)
#plt.plot(sat_09191.TIME,sat_09191.PERIGEE)
#plt.plot(sat_11682.TIME,sat_11682.PERIGEE)
#plt.plot(sat_30206.TIME,sat_30206.PERIGEE)
#plt.plot(sat_79815.TIME,sat_79815.PERIGEE)
#plt.title('perigee')
#
#plt.show()



     

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

