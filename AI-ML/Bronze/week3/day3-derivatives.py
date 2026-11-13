import sympy as sp
import numpy as np


# def gradient_descent(x, y, learning_rate, max_iterations=10000, tolerance=1e-8):
# 	"""Fit linear regression and return parameters, loss history, and iterations."""
# 	theta = np.zeros(x.shape[1], dtype=float)
# 	losses = []

# 	for iteration in range(1, max_iterations + 1):
# 		errors = x @ theta - y
# 		losses.append(np.mean(errors ** 2))
# 		gradient = (2 / len(y)) * (x.T @ errors)
# 		theta -= learning_rate * gradient

# 		if np.linalg.norm(gradient) < tolerance:
# 			break

# 	return theta, losses, iteration


# # Compare convergence speed for several learning rates.
# x_data = np.array([[1, 1], [1, 2], [1, 3], [1, 4]], dtype=float)
# y_data = np.array([3, 5, 7, 9], dtype=float)
# learning_rates = [0.001, 0.01, 0.1, 0.5]

# for rate in learning_rates:
# 	parameters, loss_history, iterations = gradient_descent(
# 		x_data, y_data, rate
# 	)
# 	print(
# 		f"Learning rate {rate}: {iterations} iterations, "
# 		f"final loss = {loss_history[-1]:.8f}, parameters = {parameters}"
# 	)



# x=sp.symbols('x')
# f=x**2+3*x+5
# derivative=sp.diff(f,x)
# second_derivative=sp.diff(derivative,x)
# print("The derivative of", f, "with respect to", x, "is:", derivative)
# print("The second derivative of", f, "with respect to", x, "is:", second_derivative)


# def gradient_descent(x,y,theta,learning_rate,iterations):
#     m=len(y)
#     for _ in range(iterations):
#         predictions=np.dot(x,theta)
#         errors=predictions-y
#         gradient=(1/m)*np.dot(x.T,errors)
#         theta=theta-learning_rate*gradient
#     return theta

# #sample dataset
# x=np.array([[1,1],[1,2],[2,2],[2,3]])
# y=np.array([1,2,2,3])
# theta=np.array([0.1,0.2])
# learning_rate=0.01
# iterations=1000
# optimal_theta=gradient_descent(x,y,theta,learning_rate,iterations)
# print("Optimal parameters:", optimal_theta)


# x,y=sp.symbols('x y')
# f=x**3+2*y**2+5*x*y+7
# partial_derivative_x=sp.diff(f,x)
# partial_derivative_y=sp.diff(f,y)

# print("The partial derivative of", f, "with respect to", x, "is:", partial_derivative_x)#gradient x
# print("The partial derivative of", f, "with respect to", y, "is:", partial_derivative_y)#gradient y

# x=sp.symbols('x')
# f=x**2+3*x+5
# derivative=sp.diff(f,x)
# print("The derivative of", f, "with respect to", x, "is:", derivative)


# x,y=sp.symbols('x y')
# f=x**2+y**2
# partial_derivative_x=sp.diff(f,x)
# partial_derivative_y=sp.diff(f,y)
# print("The partial derivative of", f, "with respect to", x, "is:", partial_derivative_x)
# print("The partial derivative of", f, "with respect to", y, "is:", partial_derivative_y)

# x=sp.symbols('x')
# f=x**2
# derivative=sp.diff(f,x)
# print("The derivative of", f, "with respect to", x, "is:", derivative)
