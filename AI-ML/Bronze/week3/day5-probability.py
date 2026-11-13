import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import poisson




# def bayes_theorem(prior,sensitivity,specificity):
#     evidence=(sensitivity*prior)+((1-specificity)*(1-prior))
#     posterior=(sensitivity*prior)/evidence
#     return posterior

# prior=0.01
# sensitivity=0.90
# specificity=0.95
# print("Posterior Probability:",bayes_theorem(prior,sensitivity,specificity))

# lam=3
# x=np.arange(0,10)
# y=poisson.pmf(x,lam)
# plt.bar(x,y)
# plt.title('Poisson Distribution')
# plt.xlabel('Number of Events')
# plt.ylabel('Probability')
# plt.show()

# n,p=10,0.5
# x=np.arange(0,n+1)
# y=binom.pmf(x,n,p)
# plt.bar(x,y)
# plt.title('Binomial Distribution')
# plt.xlabel('Number of Successes')
# plt.ylabel('Probability')
# plt.show()

# p=0.6
# plt.bar([0,1],[1-p,p],color=['blue','orange'])
# plt.title('Bernoulli Distribution')
# plt.xticks([0,1],['Failure','Success'])
# plt.xlabel('Outcome')
# plt.ylabel('Probability')
# plt.show()

# mu,sigma=0,1
# x=np.linspace(-5,5,100)
# y=1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mu)/sigma)**2)
# plt.plot(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Normal Distribution')
# plt.show()


# def bayes_theorem(prior,likelihood,evidence):
#     return (likelihood * prior) / evidence