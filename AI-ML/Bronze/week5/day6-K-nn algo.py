from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression



#load the iris dataset
data = load_iris()
x, y = data.data, data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

modellr=LogisticRegression(max_iter=200)
modellr.fit(x_train_scaled, y_train)

ypred_lr=modellr.predict(x_test_scaled)
print("Logistic Regression Accuracy:", accuracy_score(y_test, ypred_lr))

for k in range(1, 11):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train_scaled, y_train)

    y_pred=knn.predict(x_test_scaled)
    accuracy=accuracy_score(y_test, y_pred)
    print(f"Accuracy for k={k}: {accuracy:.4f}")

