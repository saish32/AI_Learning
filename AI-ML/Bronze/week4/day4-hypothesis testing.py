import numpy as np
from scipy.stats import ttest_1samp, ttest_ind
import pandas as pd

# df=pd.read_csv('https://raw.githubusercontent.com/dsrscientist/dataset1/master/iris.csv')
# sample1=df["petal length"].sample(n=30, random_state=42)
# sample2=df["petal width"].sample(n=30, random_state=42)

# t_statistic, p_value = ttest_ind(sample1, sample2)
# print("T-statistic:", t_statistic)
# print("P-value:", p_value)
# alpha=0.05
# if p_value < alpha:
#     print("Reject the null hypothesis: The two samples have significantly different means.")
# else:
#     print("Fail to reject the null hypothesis: The two samples do not have significantly different means.")

# grp1=[12, 15, 14, 10, 13]
# grp2=[18, 20, 22, 19, 21]

# t_statistic, p_value = ttest_ind(grp1, grp2)
# print("T-statistic:", t_statistic)
# print("P-value:", p_value)
# alpha=0.05

# if p_value < alpha:
#     print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
# else:
#     print("Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.")

# data = [17, 22, 31, 4, 25, 19, 28, 15, 30, 21]
# population_mean = 40
# t_statistic, p_value = ttest_1samp(data, population_mean)
# print("T-statistic:", t_statistic)
# print("P-value:", p_value)
# alpha=0.05
# if p_value < alpha:
#     print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
# else:
#     print("Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.")