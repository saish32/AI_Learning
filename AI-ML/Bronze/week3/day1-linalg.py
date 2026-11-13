import numpy as np



# block_diagonal = np.block([
# 	[np.array([[1, 2], [3, 4]]), np.zeros((2, 2))],
# 	[np.zeros((2, 2)), np.array([[5, 6], [7, 8]])],
# ])
# print("block diagonal matrix:\n", block_diagonal)


# a=np.array([[1, 2], [3, 4]])
# print(np.linalg.det(a))#determinant
# print(np.linalg.inv(a))#inverse

# i=np.eye(2)
# a=np.array([[1, 2], [3, 4]])
# print("a*i",np.dot(a,i))
# zeros=np.zeros((2,2))
# diag=np.diag([1,2,3])
# print(diag)
# print(zeros)

# a=np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
# vector=np.array([1,2,3])
# result=np.dot(a,vector)
# print("matrix multiplication \n",result)



# a=np.array([[1, 2], [3, 4]])
# b=np.array([[5, 6], [7, 8]])

# print("add \n",a+b)#add
# print("sub \n",a-b)#sub
# print("scalar multiplication \n",2*a)#scalar multiplication


# i=np.eye(2)
# zeros=np.zeros((2,2))
# diag=np.diag([1,2,3])
# print("identity matrix \n",i)
# print("zeros matrix \n",zeros)
# print("diagonal matrix \n",diag)

# print("add \n",a+b)
# print("sub \n",a-b)

# c=2*a
# print("scalar multiplication \n",c)

# print("matrix multiplication \n",np.dot(a,b))