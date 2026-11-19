from sklearn.manifold import TSNE
import numpy as np

# Sample data (e.g., points in 3D space)
data = np.array([[1, 2, 3], [1, 4, 5], [1, 0, 1],
                 [4, 2, 3], [4, 4, 5], [4, 0, 1]])

# Apply t-SNE to reduce the dimensionality of the data
tsne = TSNE(n_components=2, perplexity=5, random_state=0)#explain the parameters
# The n_components parameter specifies the number of dimensions to reduce the data to (in this case, 2D).
# The random_state parameter sets the seed for the random number generator to ensure reproducible results.

x_tsne = tsne.fit_transform(data)
# The fit_transform method computes the t-SNE embedding of the data and transforms it into the new 2D space.

print("Original data:\n", data)
print("Data after t-SNE:\n", x_tsne)
