from sklearn.ensemble import IsolationForest
import numpy as np

x=0.3*np.random.randn(100,2)
x_train=np.r_[x+2, x-2] #create training data by shifting the random data by +2 and -2
x_test=np.r_[x+2, x-2, np.random.uniform(low=-3, high=3, size=(20,2))] #create test data by adding some random noise

model=IsolationForest(n_estimators=100, contamination=0.1, random_state=42) #create an IsolationForest model with specified parameters

model.fit(x_train) #fit the model to the training data
predictions=model.predict(x_test) #predict the labels for the test data (1 for inliers, -1 for outliers)
print(predictions) #print the predictions