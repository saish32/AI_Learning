import numpy as np

# a=np.array([[1,2],[3,4]])
# i=np.eye(2)
# eigenvalue=np.linalg.eigvals(a)
# det=np.linalg.det(a-eigenvalue[0]*i)
# print(det)


#important**********
# Reduce a sample dataset from three dimensions to two using SVD.
# dataset = np.array([
# 	[2.5, 2.4, 1.2],
# 	[0.5, 0.7, 0.3],
# 	[2.2, 2.9, 1.4],
# 	[1.9, 2.2, 1.1],
# 	[3.1, 3.0, 1.6],
# 	[2.3, 2.7, 1.3],
# ])

# centered_data = dataset - np.mean(dataset, axis=0)
# u, singular_values, vt = np.linalg.svd(centered_data, full_matrices=False)
# n_components = 2
# reduced_data = u[:, :n_components] * singular_values[:n_components]

# print("Original shape:", dataset.shape)
# print("Reduced shape:", reduced_data.shape)
# print("Reduced dataset:\n", reduced_data)


# a=np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
# u,s,vt= np.linalg.svd(a)
# print("U matrix:\n", u)
# print("Singular values:\n", s)
# print("V^T matrix:\n", vt)
# #reconstruct the original matrix
# sigma=np.zeros([3,3])
# np.fill_diagonal(sigma,s)
# reconstructed=np.dot(u, np.dot(sigma, vt))
# print("Reconstructed matrix:\n", reconstructed)


# u,s,vt = np.linalg.svd(a)
# print("U matrix:\n", u)
# print("Singular values:\n", s)
# print("V^T matrix:\n", vt)

# eigenvalues, eigenvectors = np.linalg.eig(a)
# print("Eigenvalues of the matrix are:", eigenvalues)
# print("Eigenvectors of the matrix are:\n", eigenvectors)

# determinant = np.linalg.det(a)
# print("Determinant of the matrix is:", determinant)
# inverse=np.linalg.inv(a)
# print("Inverse of the matrix is:\n", inverse)
