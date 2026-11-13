import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#import titanice dataset
url='https://raw.githubusercontent.com/dsrscientist/dataset1/master/titanic_train.csv'
df=pd.read_csv(url)

# #inspect the dataset
# print(df.info())
# print(df.describe())

# #handle missing values
# df["Age"]=df["Age"].fillna(df["Age"].median())
# df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])

# #remove duplicates
# df=df.drop_duplicates()

# #filter data based on first_class passengers
# first_class_passengers = df[df["Pclass"]==1]
# print(first_class_passengers.head())

#bar graph for survival count
# survival_count=df.groupby("Pclass")["Survived"].mean()
# plt.bar(survival_count.index, survival_count.values)
# plt.title("Survival Rate by Passenger Class")
# plt.xlabel("Passenger Class")
# plt.ylabel("Survival Rate")
# plt.show()

#histogram for age distribution
# plt.hist(df["Age"], bins=20, edgecolor='black')
# plt.title("Age Distribution of Passengers")
# plt.xlabel("Age")
# plt.ylabel("Number of Passengers")
# plt.show()

#scatter plot for fare vs age
# plt.scatter(df["Age"], df["Fare"], alpha=0.5)
# plt.title("Fare vs Age of Passengers")
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.show()


