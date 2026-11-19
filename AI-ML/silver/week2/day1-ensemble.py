from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
import numpy as np
from sklearn.metrics import accuracy_score

iris=load_iris()
X=iris.data
y=iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

log_model = LogisticRegression(max_iter=200)
dt_model = DecisionTreeClassifier(random_state=42)
knn_model = KNeighborsClassifier(n_neighbors=5)

ensemble_model = VotingClassifier(estimators=[('lr', log_model), ('dt', dt_model), ('knn', knn_model)], voting='hard')
ensemble_model.fit(X_train_scaled, y_train)

y_pred_ensemble=ensemble_model.predict(x_test_scaled)
accuracy_ensemble = accuracy_score(y_test, y_pred_ensemble)

print(f"Ensemble Model Accuracy: {accuracy_ensemble:.4f}")
print("accuracy of individual models:")
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, log_model.fit(X_train_scaled, y_train).predict(x_test_scaled)):.4f}")
print(f"Decision Tree Accuracy: {accuracy_score(y_test, dt_model.fit(X_train_scaled, y_train).predict(x_test_scaled)):.4f}")
print(f"KNN Accuracy: {accuracy_score(y_test, knn_model.fit(X_train_scaled, y_train).predict(x_test_scaled)):.4f}")

