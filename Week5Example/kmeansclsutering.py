from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

data_bunch = load_iris()
x = data_bunch['data']
y = data_bunch['target']

distortion = []
iterations = range(1,10)

for p in iterations:
    kmeans_model = KMeans(n_clusters=p, random_state=1).fit(x)
    distortion.append(sum(np.min(cdist(x,kmeans_model.cluster_centers_, "euclidean"), axis = 1)/x.shape[1]))

plt.style.use("seaborn")
fig, ax = plt.subplots(num=1, nrows=1,ncols=1,clear=True)
fig.suptitle("Elbow Plot for IRis dataset for k-means")
ax.plot(iterations, distortion, marker='.',linestyle="--")
ax.set_xlabel("k Number of centroids")
ax.set_ylabel("Distortion (Mean Euclidean distances)")

kmeans_model = KMeans(n_clusters=3, random_state=1).fit(x)
predict = kmeans_model.labels_

accuracy_score(y, predict)
f1_score(y, predict, average = None)


