from statistics import mean, median, mode, stdev
import numpy as np
import scipy.stats as stats

grp1=[1.5,2.5,3.5,4.5,5.5]
grp2=[2.8,2.5,3.5,1.5,7.5]

t_statistic, p_value = stats.ttest_ind(grp1, grp2)
print("T-statistic:", t_statistic)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference between the two groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the two groups.")


# data=([1, 2, 3, 4, 5, 6, 71, 8, 9, 10])
# mean=np.mean(data)
# stdev=np.std(data )
# var=np.var(data )
# print("Mean:", mean)
# print("Standard Deviation:", stdev)
# print("Variance:", var)

# mean=mean(data)
# stdev=stdev(data)
# z_score=1.96
# ci=(mean - z_score * (stdev / (len(data) ** 0.5)), mean + z_score * (stdev / (len(data) ** 0.5)))
# print("Confidence Interval:", ci)


# data=([1, 2, 3, 4, 5, 6, 71, 8, 9, 10])
# mean=mean(data)
# median=median(data)
# mode=mode(data)
# stdev=stdev(data)
# print("Mean:", mean)
# print("Median:", median)
# print("Mode:", mode)
# print("Standard Deviation:", stdev)
# var=sum((x - mean) ** 2 for x in data) / len(data)
# print("Variance:", var)