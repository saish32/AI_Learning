from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

#create a synthetic dataset (binary classification problem, e.g., predicting whether a student passes and gets a good grade or fails based on study hours)
x= np.array([[1,50], [2,55], [3,60], [4,65], [5,70], [6,75], [7,80], [8,85], [9,90], [10,95]])
y= np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # binary labels

#split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#create and train the SVM model
model = SVC(kernel='linear', C=1.0, random_state=42)# linear kernel SVM means we are choosing linear classification boundary.
# C is the regularization parameter, which controls the trade-off between achieving a low error on the training data and minimizing the model complexity for better generalization to unseen data.
model.fit(x_train, y_train)
#make predictions
y_pred_svm = model.predict(x_test)

#evaluate the SVM model
accuracy = accuracy_score(y_test, y_pred_svm)
conf_matrix = confusion_matrix(y_test, y_pred_svm)
print(f"SVM Model Accuracy: {accuracy:.2f}")
print("Confusion Matrix:", conf_matrix)