from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

data= load_breast_cancer()
x= data.data
y= data.target

# print(f"Features: {data.feature_names}")
# print(f"Target classes: {data.target_names}")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gb_model.fit(x_train, y_train)
y_pred = gb_model.predict(x_test)

# accuracy = accuracy_score(y_test, y_pred)
# classification_rep = classification_report(y_test, y_pred)
# print(f"Gradient Boosting Model Accuracy: {accuracy:.4f}")
# print("Classification Report:", classification_rep)

# param_grid = {
#     'learning_rate': [0.01, 0.1, 0.2],
#     'n_estimators': [50, 100, 200],
#     'max_depth': [3, 5, 7]
# }
# grid_search = GridSearchCV(GradientBoostingClassifier(random_state=42), param_grid, cv=5, scoring='accuracy', n_jobs=-1)
# grid_search.fit(x_train, y_train)
# y_pred_best = grid_search.best_estimator_.predict(x_test)
# print("Best parameters found: ", grid_search.best_params_)
# print("Best cross-validation score: ", grid_search.best_score_)

# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_model.fit(x_train, y_train)
# y_pred_rf = rf_model.predict(x_test)
# accuracy_rf = accuracy_score(y_test, y_pred_rf)

# print(f"Random Forest Model Accuracy: {accuracy_rf:.4f}")
