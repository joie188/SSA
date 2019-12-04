# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:42:40 2019

@author: Brian
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

#from sat_data import gather_data

#data = gather_data("AstroYWeek3DataSet.csv", 2)

a = open('AstroYWeek3DataSet.csv')
g = a.readline()

sats = [74415, 9191, 11682, 30206,
        79815, 10814, 12605, 54494,
        55340, 58006, 75276, 87343,
        88756, 9356, 31859, 36829,
        45268, 47507, 70237, 72643,
        74562, 74866, 87337, 89581, 95609]

AstroY = {}
inc = 90
i_delta = 10
alt = 6921
alt_delta = 19

for line in a:
    line = line.split(',')
    
    sat_name = int(line[0])
    inclination = float(line[4])
    semimajor = float(line[8])
    
    if ((inc - i_delta <= inclination <= inc + i_delta) and (alt - alt_delta <= semimajor <= alt + alt_delta) or sat_name in sats) and sat_name not in AstroY:
        AstroY[sat_name] = (inclination, semimajor)
    
    
print(len(AstroY))
    