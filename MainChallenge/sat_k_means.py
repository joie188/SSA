#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.cluster import KMeans
import seaborn as sns
import sklearn.preprocessing
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

start_dict = {}

data = pd.read_csv("AstroYWeek1DataSet.csv")
current_id = 0

for i in range(len(data)):
    row = data.iloc[i]
    if row['NORAD_CAT_ID'] != current_id:
        current_id = row['NORAD_CAT_ID']
        start_dict[current_id] = [row['INCLINATION'], row['SEMIMAJOR_AXIS']]
#print(start_dict.items())
X = [data for id, data in start_dict.items()]

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
labels = kmeans.labels_

#import pdb; pdb.set_trace()

data['clusters'] = labels
cols.extend(['clusters'])

sns.lmplot('INCLINATION', 'SEMIMAJOR_AXIS', 
           data=data, 
           fit_reg=False, 
           hue="clusters",  
           scatter_kws={"marker": "D", 
                        "s": 100})
plt.show()

'''

'''
#%%
'''
df = pd.DataFrame(data, columns = ["MEAN_MOTION", 'ECCENTRICITY', 'APOGEE', 'PERIGEE', 'INCLINATION', 'RA_OF_ASC_NODE', 'ARG_OF_PERICENTER', 'MEAN_ANOMALY', 'SEMIMAJOR_AXIS', 'PERIOD'])
kmeans = KMeans(n_clusters=2)

y = kmeans.fit_predict(df[["MEAN_MOTION", 'ECCENTRICITY', 'APOGEE', 'PERIGEE', 'INCLINATION', 'RA_OF_ASC_NODE', 'ARG_OF_PERICENTER', 'MEAN_ANOMALY', 'SEMIMAJOR_AXIS', 'PERIOD']
])

df['Cluster'] = y

print(df.head())
'''
'''
data = pd.get_dummies(data, columns=['EPOCH'])


'''