import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

import sat_classifier as sc

if __name__=='__main__':
    data = sc.clustering_data()
    X = [ list(sat.orbit_param.values()) for sat in data]
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
    print(kmeans.cluster_centers_)
    print(kmeans.labels_)