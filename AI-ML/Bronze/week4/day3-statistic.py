import numpy as np
from scipy.stats import norm, t
import pandas as pd

# df=pd.read_csv('https://raw.githubusercontent.com/dsrscientist/dataset1/master/iris.csv')
# sample=df["petal length"].sample(n=30, random_state=42)
# mean=np.mean(sample)
# std_dev=np.std(sample, ddof=1)
# n=len(sample)
# z_value=norm.ppf(0.975)
# margin_of_error=z_value*(std_dev/np.sqrt(n))
# confidence_interval=(mean-margin_of_error, mean+margin_of_error)
# print("Sample Mean:", mean)
# print("Confidence Interval (95%):", confidence_interval)

# data=np.random.normal(loc=50, scale=10, size=100)
# mean=np.mean(data)
# std_dev=np.std(data, ddof=1)
# n=len(data)
# z_value=norm.ppf(0.975)
# margin_of_error=z_value*(std_dev/np.sqrt(n))
# confidence_interval=(mean-margin_of_error, mean+margin_of_error)
# print(mean)
# print(confidence_interval)


# data=[1, 2, 3, 4, 5]
# mean=np.mean(data)
# std_dev=np.std(data, ddof=1)
# n=len(data)
# t_value=t.ppf(0.975, df=n-1)
# margin_of_error=t_value*(std_dev/np.sqrt(n))
# confidence_interval=(mean-margin_of_error, mean+margin_of_error)
# print(confidence_interval)