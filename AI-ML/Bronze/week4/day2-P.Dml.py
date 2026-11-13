import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm , binom, uniform, poisson
import seaborn as sns
import pandas as pd

# df=pd.read_csv('https://raw.githubusercontent.com/dsrscientist/dataset1/master/iris.csv')

# feature=df["petal length"]
# print("skewness of petal_length:", feature.skew())
# print("kurtosis of petal_length:", feature.kurtosis())
# sns.histplot(feature, kde=True, color='blue', alpha=0.7)
# plt.title('Histogram of Petal Length with KDE')
# plt.xlabel('Petal Length')
# plt.ylabel('Frequency')
# plt.show()

# #normal distribution
# x=np.linspace(-4, 4, 1000)
# pdf=norm.pdf(x, loc=0, scale=1)
# plt.bar(x, pdf, color='blue', alpha=0.7)

# #binomial distribution
# x=np.arange(0, 11)
# pdf=binom.pmf(x, n=10, p=0.5)
# plt.bar(x, pdf, color='blue', alpha=0.7)

# #poisson distribution
# x=np.arange(0, 11)
# pdf=poisson.pmf(x, mu=3)
# plt.bar(x, pdf, color='blue', alpha=0.7)

# plt.legend(['Normal Distribution', 'Binomial Distribution', 'Poisson Distribution'])
# plt.show()

#poisson distribution
# x=np.arange(0, 11)
# pdf=poisson.pmf(x, mu=3)
# plt.bar(x, pdf, color='blue', alpha=0.7)
# plt.xlabel('x')
# plt.ylabel('Probability Mass Function')
# plt.title('Poisson Distribution PMF')
# plt.show()

#uniform distribution
# x=np.linspace(0, 1, 100)
# pdf=uniform.pdf(x, loc=0, scale=1)
# plt.plot(x, pdf, color='blue', alpha=0.7)
# plt.xlabel('x')
# plt.ylabel('Probability Density Function')
# plt.title('Uniform Distribution PDF')
# plt.show()

#binomial distribution
# x=np.arange(0, 11)
# n=10
# pdf=binom.pmf(x, n, 0.5)
# plt.bar(x, pdf, color='blue', alpha=0.7)
# plt.xlabel('x')
# plt.ylabel('Probability Mass Function')
# plt.title('Binomial Distribution PMF')
# plt.show()


## # Example 1: Normal Distribution
# x=np.linspace(-4, 4, 1000)
# pdf=norm.pdf(x, loc=0, scale=1)
# plt.plot(x, pdf, color='blue', alpha=0.7)
# plt.xlabel('x')
# plt.ylabel('Probability Density Function')
# plt.title('Normal Distribution PDF')
# plt.show()