# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 04:44:46 2019

@author: luke
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

sat_dict = {}

data = pd.read_csv("AstroYWeek2DataSet.csv")
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
from astropy import units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from poliastro.core import angles
import astropy.time

orbit_dict = {}

sat = sat_dict[9191]
for i in range(0, len(sat)):
    row = sat.iloc[i]
    ta = angles.E_to_nu(angles.M_to_E(row.MEAN_ANOMALY, row.ECCENTRICITY), row.ECCENTRICITY)

    t = astropy.time.Time(val=row.TIME, format="unix")
    orbit = Orbit.from_classical(epoch=t,
                                 attractor=Earth,
                                 a=row.SEMIMAJOR_AXIS * u.km,
                                 ecc=row.ECCENTRICITY * u.one,
                                 inc=row.INCLINATION *u.deg,
                                 raan=row.RA_OF_ASC_NODE * u.deg,
                                 argp=row.ARG_OF_PERICENTER * u.deg,
                                 nu=ta * u.deg)
    orbit_dict[row.TIME] = orbit
    
#%%
from poliastro.twobody import propagation

    