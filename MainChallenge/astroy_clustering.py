# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:19:25 2019

@author: luke
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.cluster import KMeans
import seaborn as sns
import sklearn.preprocessing
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import numpy as np

def gather_data(file):
    data = pd.read_csv(file)
    current_id = 0
    sat_data = []
    

    for i in range(len(data)):
        row = data.iloc[i]
        if row["NORAD_CAT_ID"] != current_id:
            current_id = row['NORAD_CAT_ID']
            sat_data.append(row)
            
    return sat_data

data = gather_data("AstroYWeek1DataSet.csv")
important_data = []
for sat in data:
    important_data.append([sat['INCLINATION'], sat['SEMIMAJOR_AXIS'],sat['MEAN_MOTION']])

k_means = KMeans(n_clusters=27, init='k-means++', random_state=0, )
y = k_means.fit_predict(important_data)

#%%
classes = []
for i in range(33):
    classes.append([])

for i, cluster in enumerate(y):
    classes[cluster].append(data[i]['NORAD_CAT_ID'])
        
known_sats = [74415, 9191, 11682, 30206,
        79815, 10814, 12605, 54494,
        55340, 58006, 75276, 87343,
        88756, 9356, 31859, 36829,
        45268, 47507, 70237, 72643,
        74562, 74866, 87337, 89581, 95609]

for sat in known_sats:
    for i,l in enumerate(classes):
        if sat in l:
            print(sat, i)

        
#data = pd.read_csv("AstroYWeek1DataSet.csv")
