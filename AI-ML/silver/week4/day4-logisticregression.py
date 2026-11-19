from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

#create a synthetic dataset (binary classification problem, e.g., predicting whether a student passes or fails based on study hours)
x = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # binary labels

#split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#fit the logistic regression model
logistic_model = LogisticRegression()   
logistic_model.fit(x_train, y_train)
y_pred_logistic = logistic_model.predict(x_test)

#evaluate the logistic regression model
accuracy = accuracy_score(y_test, y_pred_logistic)
conf_matrix = confusion_matrix(y_test, y_pred_logistic)
print(f"Logistic Regression Accuracy: {accuracy:.2f}")
print("Confusion Matrix:", conf_matrix)
print("Classification Report:\n", classification_report(y_test, y_pred_logistic))