import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, confusion_matrix
from imblearn.over_sampling import SMOTE

# # url="https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"

# df= pd.read_csv("C:\\Users\\LENOVO\\Downloads\\creditcard.csv")

# # print(f"dataset information: {df.info()}")
# # print(f"dataset class distribution: {df['Class'].value_counts()}")

# x=df.drop(columns=['Class'])
# y=df['Class']

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# rf_model= RandomForestClassifier(random_state=42, class_weight='balanced')
# rf_model.fit(x_train, y_train)
# y_pred= rf_model.predict(x_test)

# print(f"random forest model classification report:\n{classification_report(y_test, y_pred)}")
# print(f"random forest model roc auc score: {roc_auc_score(y_test, y_pred):.4f}")

# smote = SMOTE(random_state=42)
# x_train_smote, y_train_smote = smote.fit_resample(x_train, y_train)
# print(f"SMOTE class distribution: {pd.Series(y_train_smote).value_counts()}")

# rf_model_smote= RandomForestClassifier(random_state=42)
# rf_model_smote.fit(x_train_smote, y_train_smote)
# y_pred_smote= rf_model_smote.predict(x_test)

# print(f"random forest model with SMOTE classification report:\n{classification_report(y_test, y_pred_smote)}")
# print(f"random forest model with SMOTE roc auc score: {roc_auc_score(y_test, y_pred_smote):.4f}")


