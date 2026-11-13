from itertools import product
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# coin_tosses = np.random.choice(['H', 'T'], size=1000)
# p_heads = np.sum(coin_tosses == 'H') / len(coin_tosses)
# print("Probability of getting heads when tossing a fair coin:", p_heads)
# p_tails = np.sum(coin_tosses == 'T') / len(coin_tosses)
# print("Probability of getting tails when tossing a fair coin:", p_tails)

# x=np.linspace(0, 1, 100)
# pdf=uniform.pdf(x, loc=0, scale=1)
# plt.plot(x, pdf, color='blue', alpha=0.7)
# plt.xlabel('x')
# plt.ylabel('Probability Density Function')
# plt.title('Uniform Distribution PDF')
# plt.show()

# outcomes=np.array([1,2,3,4,5,6])
# probabilities=np.array([1/6]*6)
# plt.bar(outcomes, probabilities,color='blue', alpha=0.7)
# plt.xlabel('Outcomes')
# plt.ylabel('Probabilities')
# plt.title('Probability Distribution of Rolling a Fair Die')
# plt.show()


# rolls=np.random.randint(1,7,size=10000)
# p_even=np.sum(rolls%2==0)/len(rolls)
# print("Probability of getting an even number when rolling a fair die:", p_even)
# p_greaterthan4=np.sum(rolls>4)/len(rolls)
# print("Probability of getting a number greater than 4 when rolling a fair die:", p_greaterthan4)


# outcomes=np.array([1,2,3,4,5,6])
# probabilities=np.array([1/6]*6)
# expectation=np.sum(outcomes*probabilities)
# print("Expected value of rolling a fair die:", expectation)
# variance=np.sum((outcomes-expectation)**2*probabilities)
# print("Variance of rolling a fair die:", variance)
# std=np.sqrt(variance)
# print("Standard deviation of rolling a fair die:", std)


# sample_space=list(range(1,7))
# even_num=[2,4,6]
# p_even=len(even_num)/len(sample_space)
# print("Probability of getting an even number when rolling a fair die:", p_even)
