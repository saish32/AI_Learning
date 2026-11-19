import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# # print("dataset info")
# # print(df.info())
# # print("dataset head",df.head())

# #one_hot_encoding
# df_encoded = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
# print("\n dataset after one hot encoding",df_encoded.head())

# #Label encoding
# label_encoder = LabelEncoder()
# df['Sex'] = label_encoder.fit_transform(df['Sex'])
# print("\n dataset after label encoding",df.head())

# #apply frequency encoding
# df['ticket_freq'] = df['Ticket'].map(df['Ticket'].value_counts())
# print("\n dataset after frequency encoding")
# print(df[['Ticket', 'ticket_freq']].head())

# x = df_encoded.drop(columns=['Survived', 'Name', 'Ticket', 'Cabin'])
# x = x.fillna(x.median(numeric_only=True))
# y=df['Survived']

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model=LogisticRegression()
# model.fit(x_train, y_train)

# y_pred=model.predict(x_test)

# print("\n Accuracy score:", accuracy_score(y_test, y_pred))
