# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

sat_dict = {}

data = pd.read_csv("C:\\Users\Luke de Castro\SSA\MainChallenge\AstroYWeek1DataSet.csv")
current_id = 0

for i in range(0,len(data)):
    row = data.iloc[i]
    if row["NORAD_CAT_ID"] != current_id:
        current_id = row['NORAD_CAT_ID']
        sat_dict[current_id] = data.loc[data.NORAD_CAT_ID == current_id]
  
#%%      
from win32api import GetSystemMetrics
import comtypes

from comtypes.client import CreateObject
from comtypes.gen import STKUtil
from comtypes.gen import STKObjects
uiApplication = CreateObject('STK11.Application')
uiApplication.Visible = True
root=uiApplication.personality2

#%%
root.LoadScenario(r"C:\Users\Luke de Castro\Documents\STK 11 (x64)\MainChallenge")
sc = root.CurrentScenario
sc2 = sc.QueryInterface(STKObjects.IAgScenario)

#%%
sat = sc.Children.New(STKObjects.eSatellite, '74415')
sat2 = sat.QueryInterface(STKObjects.IAgSatellite)

#%%
