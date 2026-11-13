import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_1samp, ttest_ind
from sklearn.linear_model import LinearRegression
import seaborn as sns


# df=pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/heart_disease.csv")
# x=df['age'].values.reshape(-1, 1)
# y=df['chol'].values.reshape(-1, 1)

# model = LinearRegression()
# model.fit(x, y)

# slope = model.coef_[0][0]
# intercept = model.intercept_[0]
# r_squared = model.score(x, y)

# sns.scatterplot(x=df['age'], y=df['chol'], color='blue', label='Data points')
# plt.plot(x, model.predict(x), color='red', label='Regression line')
# plt.title('Age vs Cholesterol with Regression Line')
# plt.xlabel('Age')
# plt.ylabel('Cholesterol')
# plt.legend()
# plt.show()

# male_count = df[df['sex'] == 1].shape[0]
# female_count= df[df['sex'] == 0].shape[0]

# tstatistic, pvalue = ttest_ind(df[df['sex'] == 1]['chol'], df[df['sex'] == 0]['chol'])
# alpha = 0.05
# if pvalue < alpha:
#     print("Reject the null hypothesis: The mean cholesterol levels of males and females are significantly different.")
# else:
#     print("Fail to reject the null hypothesis: The mean cholesterol levels of males and females are not significantly different.")









# print(df.info)
# print(df.describe())

# plt.plot(df['age'], df['chol'], 'o', color='blue', label='Data points')
# plt.title('Age vs Cholesterol')
# plt.xlabel('Age')
# plt.ylabel('Cholesterol')
# plt.show()

# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix Heatmap')
# plt.show()

# sns.histplot(df['age'], kde=True, stat='density')
# plt.title('Age Heatmap')
# plt.show()

