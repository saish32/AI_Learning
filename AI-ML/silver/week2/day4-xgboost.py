import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

data= load_breast_cancer()
x= data.data
y= data.target

# print(f"Features: {data.feature_names}")
# print(f"Target classes: {data.target_names}")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#convert the data into DMatrix format for XGBoost
dtrain = xgb.DMatrix(x_train, label=y_train)
dtest = xgb.DMatrix(x_test, label=y_test)

#train the XGBoost model
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'max_depth': 3,
    'eta': 0.1
}
xgb_model= xgb.train(params, dtrain, num_boost_round=100)

y_pred = (xgb_model.predict(dtest)>0.5).astype(int)

accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
# print(f"XGBoost Model Accuracy: {accuracy:.4f}")
# print("Classification Report:", classification_rep)

param_grid = {
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

xgb_model_sklearn = XGBClassifier(objective='binary:logistic', eval_metric='logloss', random_state=42)
grid_search = GridSearchCV(xgb_model_sklearn, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(x_train, y_train)

print("Best parameters found: ", grid_search.best_params_)
print("Best cross-validation score: ", grid_search.best_score_)

gradient_boosting_model = GradientBoostingClassifier( random_state=42)
gradient_boosting_model.fit(x_train, y_train)
y_pred_gb = gradient_boosting_model.predict(x_test)
print(f"Gradient Boosting Model Accuracy: {accuracy_score(y_test, y_pred_gb):.4f}")