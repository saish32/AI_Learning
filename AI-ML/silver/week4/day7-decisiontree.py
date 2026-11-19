from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

#create a synthetic dataset (binary classification problem, e.g., predicting whether a student passes and gets a good grade or fails based on study hours)
x= np.array([[1,50], [2,55], [3,60], [4,65], [5,70], [6,75], [7,80], [8,85], [9,90], [10,95]])
y= np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # binary labels

#split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#create and train the Decision Tree model
model = DecisionTreeClassifier(random_state=42)
"""by default the Decision Tree Classifier uses the Gini impurity criterion to measure the quality of a split.
 It can also use entropy (information gain) as an alternative criterion by setting the criterion parameter to 'entropy'."""

#fit the Decision Tree model
model.fit(x_train, y_train)

#make predictions
y_pred_dt = model.predict(x_test)

#evaluate the Decision Tree model
accuracy = accuracy_score(y_test, y_pred_dt)
conf_matrix = confusion_matrix(y_test, y_pred_dt)
print(f"Decision Tree Model Accuracy: {accuracy:.2f}")
print("Confusion Matrix:", conf_matrix)