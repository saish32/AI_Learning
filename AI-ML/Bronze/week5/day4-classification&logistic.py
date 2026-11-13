import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score, recall_score, f1_score

np.random.seed(42)
nsamples = 200
x = np.random.random((nsamples, 2))
y=(x[:,0]*1.5+x[:,1]*2.0 > 0.5).astype(int).ravel()

df=pd.DataFrame(x,columns=["age","salary"])
df["purchased"]=y

x_train, x_test, y_train, y_test = train_test_split(df[["age","salary"]], df["purchased"], test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("accuracy", accuracy_score(y_test, y_pred))
print("precision", precision_score(y_test, y_pred))
print("recall", recall_score(y_test, y_pred))
print("f1", f1_score(y_test, y_pred))

xmin, xmax = x[:, 0].min() - 1, x[:, 0].max() + 1
ymin, ymax = x[:, 1].min() - 1, x[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.01),
                     np.arange(ymin, ymax, 0.01))

z=model.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)

plt.contourf(xx, yy, z, alpha=0.8, cmap="coolwarm")
plt.scatter(x_test['age'], x_test['salary'], c=y_test, cmap="coolwarm", edgecolors='black')
plt.title("Logistic Regression Decision Boundary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()



# def sigmoid(z):
#     return 1 / (1 + np.exp(-z))

# # Example usage
# z = np.linspace(-10, 10, 100)
# y = sigmoid(z)
# plt.plot(z, y)
# plt.xlabel('z')
# plt.ylabel('sigmoid(z)')
# plt.title('Sigmoid Function')
# plt.show()