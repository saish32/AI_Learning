import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# print("dataset info")
# print(df.info())
# print("dataset head",df.head())

categorical_features = df.select_dtypes(include=['str']).columns
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
# print("categorical features", categorical_features)
# print("numerical features", numerical_features)

for col in categorical_features:
    print(f"Value counts for {col}:")
    print(df[col].value_counts())
    print("\n")

print("Summary statistics for numerical features:")
print(df[numerical_features].describe())