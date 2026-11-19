from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y= iris.target

# print("info of the dataset")
# print(x.info())
# print("Target values:")
# print("target names:", iris.target_names)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

print("Accuracy without scaling:", accuracy_score(y_test, y_pred))

# scaler = MinMaxScaler()
# x_scaled = scaler.fit_transform(x)

# x_train_scaled, x_test_scaled, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)
# knn.fit(x_train_scaled, y_train)
# y_pred_scaled = knn.predict(x_test_scaled)

# print("Accuracy with MinMax scaling:", accuracy_score(y_test, y_pred_scaled))

# scaler = StandardScaler()
# x_scaled = scaler.fit_transform(x)
# x_train_scaled, x_test_scaled, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)
# knn.fit(x_train_scaled, y_train)
# y_pred_scaled = knn.predict(x_test_scaled)

# print("Accuracy with Standard scaling:", accuracy_score(y_test, y_pred_scaled))
                                                                  


