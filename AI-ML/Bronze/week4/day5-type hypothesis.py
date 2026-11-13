from scipy.stats import chi2_contingency, f_oneway, ttest_1samp, ttest_ind, ttest_rel
# import pandas as pd
# from statsmodels.formula.api import ols
# from statsmodels.stats.anova import anova_lm

# two-way ANOVA


# data = pd.DataFrame({
# 	"score": [23, 25, 24, 30, 29, 31, 35, 34, 36, 28, 27, 29],
# 	"method": ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"],
# 	"gender": ["Male", "Female"] * 6,
# })

# model = ols(
# 	"score ~ C(method) + C(gender) + C(method):C(gender)",
# 	data=data,
# ).fit()
# print("Two-way ANOVA results:")
# print(anova_lm(model, typ=2))




# #onesample t-test
# data = [17, 22, 31, 4, 25, 19, 28, 15, 30, 21]
# population_mean = 40
# t_statistic, p_value = ttest_1samp(data, population_mean)
# print("T-statistic:", t_statistic)
# print("P-value:", p_value)

# #two-sample t-test
# sample1 = [12, 15, 14, 10, 13]
# sample2 = [18, 20, 22, 19, 21]
# t_statistic, p_value = ttest_ind(sample1, sample2)
# print("T-statistic:", t_statistic)
# print("P-value:", p_value)

# #paired t-test
# pre_test = [12, 15, 14, 10, 13]
# post_test = [18, 20, 22, 19, 21]
# t_statistic, p_value = ttest_rel(pre_test, post_test)
# print("T-statistic:", t_statistic)
# print("P-value:", p_value)

# grp1 = [12, 15, 14, 10, 13]
# grp2 = [18, 20, 22, 19, 21]
# grp3 = [25, 28, 30, 27, 29]

# f_statistic, p_value = f_oneway(grp1, grp2, grp3)
# print("F-statistic:", f_statistic)
# print("P-value:", p_value)

# data=[[12,5],[29,2]]
# chi2, p, dof, expected = chi2_contingency(data)
# print("Chi-squared Statistic:", chi2)
# print("P-value:", p)
# print("Degrees of Freedom:", dof)
# print("Expected Frequencies:\n", expected)
