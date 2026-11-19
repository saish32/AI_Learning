from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

# Sample data (e.g., points in 3D space)
data = np.array([[1, 2, 3], [1, 4, 5], [1, 0, 1],
                 [4, 2, 3], [4, 4, 5], [4, 0, 1]])

# Create a DataFrame for better visualization
df = pd.DataFrame(data, columns=['Feature1', 'Feature2', 'Feature3'])

# Apply PCA to reduce the dimensionality of the data
pca = PCA(n_components=2)  # Reduce to 2D
df_pca = pca.fit_transform(df)
# The fit_transform method computes the principal components and transforms the data into the new 2D space.

print("Original data:\n", df)
print("Data after PCA:\n", df_pca)
print("Explained variance ratio:", pca.explained_variance_ratio_)