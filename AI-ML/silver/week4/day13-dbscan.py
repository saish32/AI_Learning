from sklearn.cluster import DBSCAN
import numpy as np

#sample data(eg points in 2D space)
x= np.array([[1, 2], [1, 4], [1, 0],
                 [4, 2], [4, 4], [25, 80]])

#apply DBSCAN clustering
dbscan = DBSCAN(eps=3, min_samples=2)#explain the parameters
# The eps parameter defines the maximum distance between two samples for them to be considered as in the same neighborhood.
# The min_samples parameter specifies the number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself.

dbscan.fit(x)
labels=dbscan.labels_#explain the labels
# The labels_ attribute contains the cluster labels assigned to each point in the dataset.

print("Cluster labels:", labels)