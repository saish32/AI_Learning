import pandas as pd


# data={
#     "class": ["A", "B", "A", "B", "A","C","B","C"],
#     "score": [85, 90, 78, 92, 88, 95, 80, 87],
#     "age": [15, 16, 15, 17, 16, 18, 17, 19]
# }
# df=pd.DataFrame(data)

# def var_func(x):
#     return x.max() - x.min()

# grouped=df.groupby("class")["score"].agg(var_func)
# print(grouped)


# pivot=df.pivot_table(
#     values="score",
#     index="class",
#     aggfunc="mean"
# )
# print(pivot)

# df=pd.DataFrame(data)
# print(df)

# grouped=df.groupby("class").mean()
# print(grouped)

# stats=df.groupby("class").agg({"score": ["max", "min"], "age": "max"})
# print(stats)
# grouped.mean()
# grouped.sum()

# df.groupby("category_column").agg({"numeric_column": "mean", "another_numeric_column": "sum"})
# df.groupby("category_column")["numeric_column"].agg(["mean", "sum"])

# pivot=df.pivot_table(
#     values="numeric column",
#     index="category column",
#     aggfunc="mean"
# )

# def range_func(x):
#     return x.max() - x.min()

# df.groupby("category_column")["numeric_column"].agg(range_func)

# df.groupby("category_column")["numeric_column"].max()
# df.groupby("category_column")["numeric_column"].min()
# df.groupby("category_column")["numeric_column"].mean()

# df.groupby("category_column")["numeric_column"].agg(["max", "min", "mean"])