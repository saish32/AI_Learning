from  sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

#load the iris dataset
data = load_iris()
x,y = data.data, data.target

x_test, x_train, y_test, y_train = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
cm=confusion_matrix(y_test, y_pred)
disp=ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
disp.plot(cmap=plt.cm.Blues)
plt.show()

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))





# #load the iris dataset
# data = load_iris()
# x,y = data.data, data.target
# # initialize the RandomForest Classifier
# model = RandomForestClassifier(random_state=42)
# kf=KFold(n_splits=5, shuffle=True, random_state=42)
# cv_scores = cross_val_score(model, x, y, cv=kf, scoring='accuracy')

# print("Cross-validation scores:", cv_scores)
# print("Mean CV score:", cv_scores.mean())
# print("Standard deviation of CV scores:", cv_scores.std())