import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import sat_classifier as sc
import sklearn.preprocessing
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

if __name__=='__main__':
    data = sc.clustering_data()
    X = [ list(sat.orbit_param.values()) for sat in data ]
    idontknow = [ sat.orbit_class for sat in data ]
    scaler = sklearn.preprocessing.StandardScaler()
    X = scaler.fit_transform(X)
    reduced_data = PCA(n_components=2).fit_transform(X)
    kmeans = KMeans(init='k-means++', n_clusters=5)
    kmeans.fit(reduced_data)
    theset = set()
    for i in range(len(kmeans.labels_)):
        theset.add((kmeans.labels_[i], idontknow[i]))
    print(theset)
    h = 0.02
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
            extent=(xx.min(), xx.max(), yy.min(), yy.max()),
            cmap=plt.cm.Paired,
            aspect='auto', origin='lower')

    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=169, linewidths=3,
                color='w', zorder=10)
    for i, txt in enumerate(kmeans.labels_):
        plt.annotate(txt, (reduced_data[:, 0][i], reduced_data[:, 1][i]))
    plt.title('K-means clustering (PCA-reduced data)')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.show()