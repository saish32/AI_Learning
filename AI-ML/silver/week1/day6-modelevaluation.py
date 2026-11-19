from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import  classification_report, confusion_matrix, ConfusionMatrixDisplay, mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# # regression model evaluation using mean squared error, r2 score, and mean absolute error

# data = fetch_california_housing()
# x = data.data
# y=data.target

# model=LinearRegression()
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# model.fit(x_train, y_train)
# y_pred=model.predict(x_test)

# mse=mean_squared_error(y_test, y_pred)
# r2=r2_score(y_test, y_pred)
# mae=mean_absolute_error(y_test, y_pred)

# print(f"Mean Squared Error: {mse:.2f}")
# print(f"R2 Score: {r2:.2f}")
# print(f"Mean Absolute Error: {mae:.2f}")


#classification model evaluation using confusion matrix and classification report

## Load the iris dataset
# iris = load_iris()
# x=iris.data
# y=(iris.target==0).astype(int)  # Binary classification: class 0 vs. not class 0

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model=LogisticRegression(max_iter=200)
# model.fit(x_train, y_train)
# y_pred=model.predict(x_test)

# cm=confusion_matrix(y_test, y_pred)
# disp=ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["not class 0","class 0"])
# disp.plot(cmap=plt.cm.Blues)
# plt.title("Confusion Matrix")
# plt.show()

# classification_rep=classification_report(y_test, y_pred, target_names=["not class 0","class 0"])
# print("\n Classification Report:\n", classification_rep)
