import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(42)
x=np.random.rand(100,1)*10
y=2*x+np.random.randn(100,1)*2

model=LinearRegression()
model.fit(x,y)

slope=model.coef_[0][0]
intercept=model.intercept_[0]
r_squared=model.score(x,y)

plt.scatter(x,y, color='blue', label='Data points')
plt.plot(x, model.predict(x), color='red', label='Regression line')
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# df=pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/heart_disease.csv")
# correlation_matrix = df.corr()

# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix Heatmap')
# plt.show()

# x=np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# y=np.array([5, 4, 3, 2, 1])

# model=LinearRegression()
# model.fit(x,y)
# print(f"slope: {model.coef_[0]}")
# print(f"intercept: {model.intercept_}")
# print(f"Coefficient of determination (R^2): {model.score(x,y)}")

# x=np.array([1, 2, 3, 4, 5])
# y=np.array([5, 4, 3, 2, 1])

# # Calculate Pearson correlation coefficient
# pearson_corr, _ = pearsonr(x, y)

# # Calculate Spearman correlation coefficient
# spearman_corr, _ = spearmanr(x, y)

# print(f"Pearson correlation coefficient: {pearson_corr}")
# print(f"Spearman correlation coefficient: {spearman_corr}")