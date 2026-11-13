import numpy as np

#generate synthetic data
np.random.seed(42)
x=2*np.random.rand(100,1)  # x: 100 random values between 0 and 2 (features/independent variable)
y=4+3*x+np.random.randn(100,1)  # y: linear relationship y=4+3x with random noise (target/dependent variable)

#add bias term
X_b=np.c_[np.ones((100,1)),x]  # add bias term (intercept) to the features

#initialize parameters
theta=np.random.randn(2,1) 
learning_rate=0.01# random initialization of parameters (weights)
iterations=1000  # number of iterations for gradient descent

def predict(x, theta):
    return x.dot(theta)

#use gradient descent to optimize parameters
def gradient_descent(X, y, theta, learning_rate, iterations):
    m=len(y)
    for iteration in range(iterations):
        gradients=1/m*X.T.dot(predict(X, theta)-y)  # compute gradients
        theta=theta-learning_rate*gradients  # update parameters
    return theta

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true-y_pred)**2)  # compute mean squared error

def r_squared(y_true, y_pred):
    ss_total=np.sum((y_true-np.mean(y_true))**2)  # total sum of squares
    ss_residual=np.sum((y_true-y_pred)**2)  # residual sum of squares
    return 1-(ss_residual/ss_total)  # compute R-squared

theta_optimized=gradient_descent(X_b, y, theta, learning_rate, iterations)  # optimize parameters using gradient descent
y_pred=predict(X_b, theta_optimized)  # make predictions using optimized parameters 
mse=mean_squared_error(y, y_pred)  # compute mean squared error
r2=r_squared(y, y_pred)  # compute R-squared
print("Optimized Parameters (theta):", theta_optimized)
print("Mean Squared Error:", mse)
print("R-squared:", r2)