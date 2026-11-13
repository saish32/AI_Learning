import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier




# data=fetch_california_housing(as_frame=True)
# df=data.frame

# print(df.info())
# print(df.describe())

# x=df[['MedInc','HouseAge','AveRooms']]
# y=df['MedHouseVal']

# sns.pairplot(df,vars=['MedInc', 'HouseAge', 'AveRooms', 'AveOccup', 'MedHouseVal'])
# plt.show()

# print("missing values in each column:" , df.isnull().sum())

# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
# model=LinearRegression()
# model.fit(x_train,y_train)

# y_pred=model.predict(x_test)

# print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
# print("R2 Score:", r2_score(y_test, y_pred))


#load telco customer churn dataset
# telco_df=pd.read_csv("telco-customer-churn.csv")

# print(telco_df.info())
# print(telco_df.describe())

# sns.countplot(x='Churn',data=telco_df)
# plt.title("Count of Churned vs Non-Churned Customers")
# plt.show()

# telco_df.fillna(telco_df.mean(), inplace=True)

# le=LabelEncoder()
# telco_df['churn']=le.fit_transform(telco_df['Churn'])

# x=telco_df.drop(['customerID','Churn','churn'],axis=1)
# y=telco_df['churn']

# scaler=StandardScaler()
# x_scaled=scaler.fit_transform(x)

# x_train, x_test, y_train, y_test = train_test_split(x_scaled,y,test_size=0.2,random_state=42)

# log_model=LogisticRegression(max_iter=200)
# log_model.fit(x_train,y_train)

# y_pred=log_model.predict(x_test)

# knn_model=KNeighborsClassifier(n_neighbors=5)
# knn_model.fit(x_train,y_train)

# y_pred_knn=knn_model.predict(x_test)

# print("Logistic Regression Classification Report:\n", classification_report(y_test, y_pred))
# print("Logistic Regression Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# print("K-Nearest Neighbors Classification Report:\n", classification_report(y_test, y_pred_knn))
# print("K-Nearest Neighbors Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))



