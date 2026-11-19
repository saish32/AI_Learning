from sklearn.mixture import GaussianMixture
import numpy as np

# Sample data (e.g., points in 2D space)
data = np.array([[1, 2], [1, 4], [1, 0],
                 [4, 2], [4, 4], [25, 80]])

# Fit a Gaussian Mixture Model with 2 components
gmm = GaussianMixture(n_components=2, random_state=0)#explain the parameters
# The n_components parameter specifies the number of mixture components (clusters) to fit.
# The random_state parameter sets the seed for the random number generator to ensure reproducible results.

gmm.fit(data)
labels = gmm.predict(data)#explain the labels
# The predict method assigns each data point to one of the mixture components (clusters) based on the fitted model.
gmm_predict_probabilities = gmm.predict_proba(data)#explain the probabilities
# The predict_proba method returns the probabilities of each data point belonging to each of the mixture components (clusters).

print("Cluster labels:", labels)
print("Cluster probabilities:\n", gmm_predict_probabilities)