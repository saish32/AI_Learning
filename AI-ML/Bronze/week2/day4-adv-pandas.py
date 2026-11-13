import pandas as pd
import numpy as np



 
# df2=pd.DataFrame({
#     "Id":[1,2,3],
#     "Score":[85,90,95]
# })
# print(df1)
# print(df2)

# merged=pd.merge(df1,df2,how="inner",on="Id")#merge two dataframes on Id
# print("merged DataFrame:",merged)
# merged["score percentage"]=merged["Score"]/100*100#add new column to merged dataframe
# print("merged DataFrame with new column:\n",merged)



# data={
#     "name":["Alice","Bob",np.nan,"David","Eva"],
#     "age":[25,30,35,np.nan,45],
#     "score":[85,np.nan,95,80,75]
# }
# df=pd.DataFrame(data)
# print(df)

# df["age"]=df["age"].fillna(df["age"].mean())#fill missing values with mean
# df["score"]=df["score"].interpolate()#interpolate missing values
# df=df.rename(columns={"name":"Name","age":"Age","score":"Score"})#rename columns
# print(df)



# combined=pd.concat([df1,df2],axis=0)#combine two dataframes vertically
# combined=pd.concat([df1,df2],axis=1)#combine two dataframes horizontally

# merged=pd.merge(df1,df2,on="column name")#merge two dataframes on column name
# merged=pd.merge(df1,df2,how="inner",on="column name")#merge two dataframes on column name with inner join

# joined=df1.join(df2.set_index("column name"),on="column name")#join two dataframes on column name

# df=df.rename(columns={"old column name":"new column name"})#rename column

# df[column name]=df[column name].astype("int")#change data type of column to int
# df[column name]=pd.to_datetime(df[column name])#change data type of column to datetime
# df["new column name"]=df["column name"].apply(lambda x:x*2)#apply function to column
# df["new column name"]=df["column name"]*2#apply function to column


# df=df.dropna()#drop rows with missing values
# df=df.dropna(axis=1)#drop columns with missing values

# df["column name"]=df["column name"].fillna(0)#fill missing values with 0

# df.fillna(method="ffill")#fill missing values with previous value
# df.fillna(method="bfill")#fill missing values with next value

# df["column name"]=df["column name"].replace("old value","new value")#replace old value with new value
# df["column name"]=df["column name"].str.strip()#remove leading and trailing whitespace
# df["column name"]=df["column name"].str.lower()#convert to lowercase
# df["column name"]=df["column name"].str.upper()#convert to uppercase
# df["column name"]=df["column name"].interpolate()#interpolate missing values