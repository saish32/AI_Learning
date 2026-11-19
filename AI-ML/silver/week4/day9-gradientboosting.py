from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

#create a synthetic dataset (binary classification problem, e.g., predicting whether a student passes and gets a good grade or fails based on study hours)
x= np.array([[1,50], [2,55], [3,60], [4,65], [5,70], [6,75], [7,80], [8,85], [9,90], [10,95]])
y= np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # binary labels

#split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#train the Gradient Boosting model
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
"""The n_estimators parameter specifies the number of boosting stages to be run. A higher number of stages can improve the model's performance but also increases computational cost.
 The learning_rate parameter controls the contribution of each tree to the final prediction. A lower learning rate requires more trees to achieve the same level of performance."""

#fit the Gradient Boosting model
model.fit(x_train, y_train)
y_pred_gb = model.predict(x_test)

#evaluate the Gradient Boosting model
accuracy = accuracy_score(y_test, y_pred_gb)
conf_matrix = confusion_matrix(y_test, y_pred_gb)
print(f"Gradient Boosting Model Accuracy: {accuracy:.2f}")
print("Confusion Matrix:", conf_matrix)