import pandas as pd
# from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/heart_disease.csv")
# features=df[['age', 'sex']]
# target=df['chol']
# print("Features:\n", features.head())
# print("\nTarget:\n", target.head())

# x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
# print("\nTraining set:\n", x_train.head())
# print("\nTest set:\n", x_test.head())
# print("\nTraining target:\n", y_train.head())
# print("\nTest target:\n", y_test.head())

# sns.pairplot(df,x_vars=['age', 'sex'], y_vars=['chol'], hue='target', height=3,kind='scatter')
# plt.legend(title='Target', loc='upper right')
# plt.show()
