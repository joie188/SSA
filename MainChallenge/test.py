import pandas as pd
satellite_data = pd.read_csv('AstroYWeek1DataSet.csv')
satellite_dict = dict()
print(satellite_data.head())
'''
from win32api import GetSystemMetrics
from IPython.display import Image, display, SVG
import os as os
import comtypes
from comtypes.client import CreateObject

app=CreateObject("STK11.Application")
app.Visible=True
app.UserControl= True
root=app.Personality2

from comtypes.gen import STKUtil
from comtypes.gen import STKObjects

root.NewScenario("IPython_DIY")
sc=root.CurrentScenario
sc2=sc.QueryInterface(STKObjects.IAgScenario)
sc2.SetTimePeriod("10 Jun 2016 04:00:00","11 Jun 2016 04:00:00")
root.Rewind()'''