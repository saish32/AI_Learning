from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
import numpy as np
import matplotlib.pyplot as plt

# Sample data (e.g., points in 2D space)
data = np.array([[1, 2], [1, 4], [1, 0],
                 [4, 2], [4, 4], [4, 0]])

# Perform hierarchical clustering using the 'ward' method
Z = linkage(data, method='ward')#explain the linkage
# The linkage function performs hierarchical clustering on the input data.
# The 'ward' method minimizes the variance of the clusters being merged.

# Plot the dendrogram
#explain the dendrogram
# A dendrogram is a tree-like diagram that illustrates the arrangement of the clusters produced by hierarchical clustering. 
# The height of each node in the dendrogram represents the distance at which the clusters were merged.

plt.figure(figsize=(10, 5))
dendrogram(Z, labels=np.arange(len(data)), leaf_rotation=90, leaf_font_size=12)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()

