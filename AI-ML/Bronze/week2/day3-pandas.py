import pandas as pd

# df=pd.read_csv("any csv/excel file")

# filtered_rows=df[df['column name']>value & df['column name']<value]
# filtered_rows.to_csv("output.csv",index=False)

# dict={"name":["alice","bob","sam"],"age":["24","30","35"]}
# df1=pd.DataFrame(dict)
# df1_add_column=df1.assign(salary=[50000,60000,70000])
# print("dataframe with new column\n",df1_add_column)

#explore the data for csv/excel file
# print("first five row",df.head())
# print("last five row",df.tail())
# print("info",df.info())
# print("describe",df.describe())

# selected_column=df['column name',"column name"]
# filtered_rows=df[df['column name']>value & df['column name']<value]
# print("selected column",selected_column)
# print("filtered rows",filtered_rows)


# # Sample DataFrame for demonstration
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40]
# }
# df = pd.DataFrame(data)

# print(df.head())  # Display the first 5 rows of the DataFrame
# print(df.tail())  # Display the last 5 rows of the DataFrame

# print(df.info())  # Display information about the DataFrame, including column names, data types, and non-null counts
# print(df.describe())  # Display summary statistics for numerical columns in the DataFrame

# print(df['Name'])  # Access a specific column (Series) by column name
# print(df[['Name', 'Age']])  # Access multiple columns (DataFrame) by column names
# print(df[df['Age'] > 30])  # Filter rows based on a condition

# print(df.iloc[0])  # Access a specific row by index position
# print(df.iloc[:0])  # Access a range of rows by index positions

# print(df.loc[0])  # Access a specific row by index label
# print(df.loc[:, 'Name'])  # Access a range of rows and specific columns by index labels
# s=pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(s)

#     'Age':[25, 30, 35, 40]
# }
# df=pd.DataFrame(data)
# print(df)


# #load and save data csv/excel
# df=pd.read_csv('data.csv')
# df=pd.read_excel('data.xlsx')
# df.to_csv('output.csv', index=False)
# df.to_excel('output.xlsx', index=False)