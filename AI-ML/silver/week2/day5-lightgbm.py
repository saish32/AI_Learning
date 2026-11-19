import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import lightgbm as lgb
from sklearn.metrics import accuracy_score, classification_report
from catboost import CatBoostClassifier
from xgboost import XGBClassifier


# df= pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# features= ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
# target= 'Survived'

# df.fillna({'Age': df['Age'].median(), 'Fare': df['Fare'].median()}, inplace=True)
# df.fillna({'Embarked': df['Embarked'].mode()[0]}, inplace=True)

# label_encoder ={}
# for col in ['Sex', 'Embarked']:
#     le= LabelEncoder()
#     df[col]= le.fit_transform(df[col])
#     label_encoder[col]= le

# x= df[features]
# y= df[target]

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# print(f"Training set shape: {x_train.shape}, {x_test.shape}")

# lgb_model= lgb.LGBMClassifier( random_state=42)
# lgb_model.fit(x_train, y_train)
# y_pred= lgb_model.predict(x_test)
# print(f"LightGBM Model Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# cat_features= ['Pclass', 'Sex', 'Embarked']
# catboost_model= CatBoostClassifier(cat_features=cat_features, verbose=0)
# catboost_model.fit(x_train, y_train)
# y_pred_cb= catboost_model.predict(x_test)
# print(f"CatBoost Model Accuracy: {accuracy_score(y_test, y_pred_cb):.4f}")

# xgb_model= XGBClassifier(eval_metric='logloss', random_state=42)
# xgb_model.fit(x_train, y_train)
# y_pred_xgb= xgb_model.predict(x_test)
# print(f"XGBoost Model Accuracy: {accuracy_score(y_test, y_pred_xgb):.4f}")

# catboost_native_model= CatBoostClassifier(cat_features=['Sex', 'Embarked'], verbose=0)
# catboost_native_model.fit(x_train, y_train)
# y_pred_cb_native= catboost_native_model.predict(x_test)
# print(f"CatBoost Native Model Accuracy: {accuracy_score(y_test, y_pred_cb_native):.4f}")