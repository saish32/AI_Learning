from sklearn.cluster import KMeans
import numpy as np

#sample data(eg points in 2D space)
data = np.array([[1, 2], [1, 4], [1, 0],
                 [4, 2], [4, 4], [4, 0]])

#apply K-means clustering
kmeans = KMeans(n_clusters=2, random_state=42)
"""n_clusters specifies the number of clusters to form and the number of centroids to generate. 
The random_state parameter ensures reproducibility of the results by setting a seed for the random number generator."""

kmeans.fit(data)
labels = kmeans.labels_#explain the labels
# The labels array contains the cluster assignments for each data point.
# Each element in the array corresponds to the cluster number (0 or 1) that the respective data point belongs to.
centroids = kmeans.cluster_centers_#explain the centroids
# The centroids array contains the coordinates of the cluster centers.

print("Data points:", data)
print("Cluster labels:", labels)
print("Centroids:", centroids)

