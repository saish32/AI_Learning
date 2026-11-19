from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# diabetes=load_diabetes()
# df=pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
# df['target']=diabetes.target

# print("dataset info", df.info())
# print("dataset description", df.describe())
# print("dataset head", df.head())

# corr_matrix = df.corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title("Correlation Matrix")
# plt.show()

# corelkated_feature=corr_matrix['target'].sort_values(ascending=False)
# print("\n Correlation with target variable:\n", corelkated_feature)

# x=df.drop(columns=['target'])
# y=df['target']

# mutual_info = mutual_info_regression(x, y)

# #create a dataframe for better visualization
# mutual_info_df = pd.DataFrame({'Feature': x.columns, 'Mutual Information': mutual_info})
# mutual_info_df = mutual_info_df.sort_values(by='Mutual Information', ascending=False)

# print("\n Mutual Information Scores:\n", mutual_info_df)

# model=RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(x, y)

# feature_importance=model.feature_importances_
# imporatnt_features_df=pd.DataFrame({'Feature': x.columns, 'Importance': feature_importance})
# imporatnt_features_df=imporatnt_features_df.sort_values(by='Importance', ascending=False)
# print("\n Feature Importance:\n", imporatnt_features_df)

# plt.figure(figsize=(10, 6))
# plt.barh(imporatnt_features_df['Feature'], imporatnt_features_df['Importance'])
# plt.gca().invert_yaxis()  # Invert y-axis to have the most important feature on top
# plt.xlabel('Importance')
# plt.ylabel('Feature')
# plt.title('Feature Importance from Random Forest Regressor')
# plt.show()
