from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

#create a synthetic dataset(house prices based on square footage)
x=np.array([[275],[300],[350],[400],[450],[500],[550],[600],[650],[700]])
y=np.array([23, 26, 30, 35, 40, 45, 50, 55, 60, 65])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#ridge regression
ridge_model=Ridge(alpha=1.0)
ridge_model.fit(x_train,y_train)
ridge_y_pred=ridge_model.predict(x_test)

#evaluate the ridge model
ridge_mse=mean_squared_error(y_test,ridge_y_pred)
print(f"Ridge Mean Squared Error: {ridge_mse:.2f}")

#lasso regression
lasso_model=Lasso(alpha=0.1)
lasso_model.fit(x_train,y_train)
y_pred_lasso=lasso_model.predict(x_test)

#evaluate the lasso model
lasso_mse=mean_squared_error(y_test,y_pred_lasso)
print(f"Lasso Mean Squared Error: {lasso_mse:.2f}")