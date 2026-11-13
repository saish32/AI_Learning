import sympy as sp
import numpy as np



#generate synthetic data
# np.random.seed(42)
# x=2*np.random.rand(100,1)
# y=3*x+2+np.random.randn(100,1)*0.1

# #add bias term to x
# x_bias=np.c_[np.ones((100,1)),x]

# #sgd implementation
# def sgd(x,y,theta,learning_rate=0.01,iterations=1000):
#     m=len(y)
#     for _ in range(iterations):
#         for i in range(m):
#             random_index=np.random.randint(m)
#             xi=x[random_index:random_index+1]
#             yi=y[random_index:random_index+1]
#             gradients=2*xi.T.dot(xi.dot(theta)-yi)
#             theta=theta-learning_rate*gradients
#     return theta

# #initialize_parameters
# theta=np.random.randn(2,1)
# optimal_theta=sgd(x_bias,y,theta)
# print("Optimal parameters:", optimal_theta)

# Define the variable
# x = sp.symbols('x')
# f=x**2
# definite_integral = sp.integrate(f, (x, 0, 2))
# indefinite_integral = sp.integrate(f, x)
# print("The definite integral of", f, "from 0 to 2 is:", definite_integral)
# print("The indefinite integral of", f, "is:", indefinite_integral)