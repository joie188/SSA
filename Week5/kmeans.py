# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:30:33 2019

@author: Brian
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
sats = ['ABS-3A_40424_Inclination&SMA.csv',
        'EUTELSAT_115_WEST_B_40425_Inclination&SMA.csv',
        'EUTELSAT_8_WEST_B_40875_Inclination&SMA.csv',
        'G25_24812_Inclination&SMA.csv',
        'INMARSAT_5-F1_39476_Inclination&SMA.csv',
        'INTELSAT_29E_IS-29E_41308_Inclination&SMA.csv',
        'Intelsat28_37392_Inclination&SMA.csv',
        'Satmex8_39122_Inclination&SMA.csv',
        'Ses1_36516_Inclination&SMA.csv',
        'Telstar401_22927_Inclination&SMA.csv']
f = pd.read_csv('ABS-3A_40424_Inclination&SMA.csv').values
a, i = np.transpose(f)


#kmeans = KMeans(3)
#kmeans.fit(f)
#plt.plot(kmeans)

line = [i for i in range(len(a))]
#plt.plot(line, a)
plt.plot(line, [(data-a[0])/a[0] for data in a])
plt.plot(line, [(data-i[0])/i[0] for data in i])