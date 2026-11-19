from operator import mul
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, confusion_matrix

url="https://raw.githubusercontent.com/KimathiNewton/Telco-Customer-Churn/master/Datasets/telco_churn.csv"

df= pd.read_csv(url)
# print(f"dataset information: {df.info()}")
# print(f"dataset class distribution: {df['Churn'].value_counts()}")

# print(f"dataset missing values: {df.isnull().sum()}")

print(df['Churn'].value_counts())
print(df['Churn'].unique())
print(df['Churn'].head(20))

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.fillna({'TotalCharges': df['TotalCharges'].median()}, inplace=True)

label_encoder = LabelEncoder()
for column in df.select_dtypes(include=['str']).columns:
    if column != 'Churn':
        df[column] = label_encoder.fit_transform(df[column])

df['Churn'] = df['Churn'].map({
    'False': 0,
    'No': 0,
    'True': 1,
    'Yes': 1
})

df = df.dropna(subset=['Churn'])

df['Churn'] = df['Churn'].astype(int)

scaler = StandardScaler()
numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
df[numerical_features] = scaler.fit_transform(df[numerical_features])

x= df.drop(columns=['Churn'])
y= df['Churn']

x.columns = [f"feature_{i}" for i in range(x.shape[1])]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#apply SMOTE to balance the dataset
smote = SMOTE(random_state=42)
x_resampled, y_resampled = smote.fit_resample(x_train, y_train)

# print(f"Original class distribution:\n{y_train.value_counts()}")
# print(f"Resampled class distribution:\n{pd.Series(y_resampled).value_counts()}")



#train and evaluate Random Forest Classifier

rf_model= RandomForestClassifier(random_state=42)
rf_model.fit(x_resampled, y_resampled)
y_pred_rf= rf_model.predict(x_test)
print(f"random forest model roc-auc score: {roc_auc_score(y_test, rf_model.predict_proba(x_test)[:, 1]):.4f}")



#train and evaluate XGBoost Classifier
xgb_model= XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
xgb_model.fit(x_resampled, y_resampled)
y_pred_xgb= xgb_model.predict(x_test)
print(f"xgboost model roc-auc score: {roc_auc_score(y_test, xgb_model.predict_proba(x_test)[:, 1]):.4f}")

#train and evaluate LightGBM Classifier
lgbm_model= LGBMClassifier(random_state=42) 
lgbm_model.fit(x_resampled, y_resampled)
y_pred_lgbm= lgbm_model.predict(x_test)
print(f"lightgbm model roc-auc score: {roc_auc_score(y_test, lgbm_model.predict_proba(x_test)[:, 1]):.4f}")

