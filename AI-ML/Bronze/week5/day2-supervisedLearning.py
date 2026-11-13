import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# #generate a random dataset
# np.random.seed(42)
# x=np.random.rand(100, 1) * 10  # 100 random values between 0 and 10
# y=3 * x + np.random.randn(100, 1) * 2  # linear relation with some noise

# xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
# model = LinearRegression()
# model.fit(xtrain, ytrain)

# ypred = model.predict(xtest)

# print("Mean Squared Error:", mean_squared_error(ytest, ypred))
# print("R2 Score:", r2_score(ytest, ypred))


# plt.scatter(xtest, ytest, color='blue', label='Actual')
# plt.plot(xtest, ypred, color='red', linewidth=2, label='Predicted')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Linear Regression')
# plt.legend()
# plt.show()
