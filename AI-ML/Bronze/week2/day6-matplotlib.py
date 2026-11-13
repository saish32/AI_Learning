# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# import pandas as pd

# df=pd.read_csv('https://raw.githubusercontent.com/dsrscientist/dataset1/master/iris.csv')

# del df['class']

# coorelation_matrix=df.corr()

# sns.heatmap(coorelation_matrix,annot=True,cmap='coolwarm')
# plt.title('Heatmap Example')
# plt.show()


#scatter plot
# study_hours = [1, 2, 3, 4, 5]
# test_scores = [50, 60, 70, 80, 90]
# plt.scatter(study_hours, test_scores, color='blue', marker='o')
# plt.title('Scatter Plot Example')
# plt.xlabel('Study Hours')
# plt.ylabel('Test Scores')
# plt.legend(['Test Scores vs Study Hours'])
# plt.show()

#barplot
# categories = ['A', 'B', 'C', 'D']
# values = [10, 15, 7, 12]
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Bar Plot Example')
# plt.bar(categories, values, color='blue')
# plt.show()

#line plot
# sem=[1,2,3,4]
# cgpa=[8.57,9.23,8.82,9.45]
# plt.title('Line Plot Example')
# plt.xlabel('Semester')
# plt.ylabel('CGPA')
# plt.plot(sem, cgpa, marker='o', color='blue', linestyle='-', linewidth=2)
# plt.legend(['CGPA Trend'])
# plt.show()


# data=np.random.rand(5,5)
# sns.heatmap(data,annot=True,cmap='coolwarm')
# plt.title('Heatmap Example')
# sns.pairplot(df)
# plt.show()


#scatter plot
# x = [1, 2, 3, 4, 5]
# y=[2, 3, 5, 7, 11]
# plt.title("scatter plot example")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.scatter(x, y, color='red', marker='x')
# plt.show()

#bar plot
# x = ['A', 'B', 'C', 'D']
# y=[10, 15, 7, 12]
# plt.title('Bar Plot Example')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.bar(x,y,color='blue')
# plt.show()


# Sample data
# x = [1, 2, 3, 4, 5]
# y=[2, 3, 5, 7, 11]
# plt.plot(x,y)
# plt.show()

#line plot
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],label='trend',marker='o',color='green',linestyle='--')
# plt.title('Line Plot Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.show()
