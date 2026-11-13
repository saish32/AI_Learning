import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# data = fetch_california_housing(as_frame=True)
# df=data.frame
# x=df[['MedInc']].values
# y=df['MedHouseVal'].values

# polynomial_features = PolynomialFeatures(degree=2)
# x_poly = polynomial_features.fit_transform(x)

# x_train, x_test, y_train, y_test = train_test_split(x_poly, y, test_size=0.2, random_state=42)

# ridge_model = Ridge(alpha=1.0)
# ridge_model.fit(x_train, y_train)
# ridge_pred = ridge_model.predict(x_test)

# lasso_model = Lasso(alpha=0.1)
# lasso_model.fit(x_train, y_train)
# lasso_pred = lasso_model.predict(x_test)

# ridge_mse = mean_squared_error(y_test, ridge_pred)
# lasso_mse = mean_squared_error(y_test, lasso_pred)
# print("Ridge Mean Squared Error:", ridge_mse)
# print("Lasso Mean Squared Error:", lasso_mse)

# model=LinearRegression()
# model.fit(x_poly,y)
# y_pred=model.predict(x_poly)

# plt.scatter(x, y, color='blue', label='Actual data')
# plt.scatter(x, y_pred, color='red', label='Predicted data')
# plt.legend()
# plt.xlabel('Median Income')
# plt.ylabel('Median House Value')
# plt.title('Polynomial Regression on California Housing Data')
# plt.show()

# mse=mean_squared_error(y, y_pred)
# print("Mean Squared Error:", mse)

#generate some sample data
# np.random.seed(0)
# x=np.random.rand(100, 1) * 10
# y = 2 * x**2 + 3 * x + 5 + np.random.randn(100, 1) * 10


# poly_features = PolynomialFeatures(degree=2)
# x_poly = poly_features.fit_transform(x)

# xtrain,xtest,ytrain,ytest = train_test_split(x_poly,y,test_size=0.2,random_state=42)

# ridge_model = Ridge(alpha=1.0)
# ridge_model.fit(xtrain, ytrain)
# ridge_pred = ridge_model.predict(xtest)

# lasso_model = Lasso(alpha=0.1)
# lasso_model.fit(xtrain, ytrain)
# lasso_pred = lasso_model.predict(xtest)

# ridge_mse = mean_squared_error(ytest, ridge_pred)
# lasso_mse = mean_squared_error(ytest, lasso_pred)
# print("Ridge Mean Squared Error:", ridge_mse)
# print("Lasso Mean Squared Error:", lasso_mse)



# print("Original data shape:", x.shape)
# print("Polynomial data shape:", x_poly.shape)

# model = LinearRegression()
# model.fit(x_poly, y)
# y_pred = model.predict(x_poly)

# plt.scatter(x, y, color='blue', label='Actual data')
# plt.scatter(x, y_pred, color='red', label='Predicted data')
# plt.legend()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Polynomial Regression')
# plt.show()

# mse=mean_squared_error(y, y_pred)
# print("Mean Squared Error:", mse)