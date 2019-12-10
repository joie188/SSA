# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:15:42 2019

@author: luke
"""

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
    astroy_sats = [68, 5855, 6916, 8333, 8740, 9140, 9191, 9356, 9594, 10814, 
                   10970, 11349, 11682, 12309, 12605, 15228, 15632, 15956, 16204, 
                   16224, 16314, 16617, 18742, 21061, 24468, 24863, 26864, 27643, 
                   28692, 30000, 30206, 31859, 33499, 33960, 34077, 36829, 37538, 
                   38025, 38967, 39591, 44093, 44896, 45105, 45268, 45935, 46729,
                   47507, 49231, 50450, 52822, 53207, 54494, 55041, 55340, 57872,
                   58006, 59114, 60283, 63646, 65215, 65817, 68564, 69128, 70082,
                   70237, 70502, 71823, 71909, 72643, 74562, 74796, 74866, 74906,
                   75276, 76684, 79359, 79606, 79712, 79815, 79991, 81683, 83471, 
                   86077, 86116, 86892, 87168, 87337, 87343, 88150, 88756, 88819, 
                   88854, 89581, 93428, 93836, 95609, 95991, 96484, 96564, 99277,
                   7288, 16569, 34614, 47719,74415] #remove 74415

    for i in range(len(data)):
        row = data.iloc[i]
        if row["NORAD_CAT_ID"] != current_id and row['NORAD_CAT_ID'] in astroy_sats:
            current_id = row['NORAD_CAT_ID']
            sat_data.append(row)
            
    return sat_data

data = gather_data("AstroYWeek1DataSet.csv")
important_data = []
for sat in data:
    important_data.append([sat['RA_OF_ASC_NODE']])

k_means = KMeans(n_clusters=7, init='k-means++', random_state=0, )
y = k_means.fit_predict(important_data)

#%%
classes = []
for i in range(7):
    classes.append([])

for i, cluster in enumerate(y):
    classes[cluster].append(data[i]['NORAD_CAT_ID'])
        
known_sats = [74415, 9191, 11682, 30206,
        79815, 10814, 12605, 54494,
        55340, 58006, 75276, 87343,
        88756, 9356, 31859, 36829,
        45268, 47507, 70237, 72643,
        74562, 74866, 87337, 89581, 95609]

count = [0,0,0,0,0,0,0]

for sat in known_sats:
    for i,l in enumerate(classes):
        if sat in l:
            count[i] += 1
            print(sat, i)

        
#data = pd.read_csv("AstroYWeek1DataSet.csv")