from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

#create a synthetic dataset(employee salaries based on years of experience)
x=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y=np.array([30000, 35000, 400000, 45000, 550000, 65000, 75000, 85000, 95000, 1705000])

#split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#transform the features to polynomial features
poly_features = PolynomialFeatures(degree=2)
x_train_poly = poly_features.fit_transform(x_train)
x_test_poly = poly_features.transform(x_test)

#fit the linear regression model
linear_model = LinearRegression()
linear_model.fit(x_train_poly, y_train)

#make predictions
y_pred = linear_model.predict(x_test_poly)

#evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")