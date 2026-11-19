import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# df=pd.read_csv("bike_sharing.csv")
# print("dataset info", df.info())
# print("dataset head", df.head())

##convert dteday to datetime
# df['dteday'] = pd.to_datetime(df['dteday'])
# df["day-of-week"] = df['dteday'].dt.day_name()
# df["month"] = df['dteday'].dt.month_name()
# df["year"] = df['dteday'].dt.year

# print("\n dataset after extracting day-of-week, month, and year")
# print(df[['dteday', 'day-of-week', 'month', 'year']].head())

# x=df['temp']
# y=df['cnt']

# poly_features = PolynomialFeatures(degree=2,include_bias=False)
# x_poly = poly_features.fit_transform(x.values.reshape(-1, 1))
# print("\n original and polynomial feature ")
# print(pd.DataFrame(x_poly, columns=['temp', 'temp^2']).head())

# x_train, x_test, y_train, y_test = train_test_split(x_poly, y, test_size=0.2, random_state=42)
# x_poly_train, x_poly_test = train_test_split(x_poly, test_size=0.2, random_state=42)

# model=LinearRegression()
# model.fit(x_train, y_train)
# y_pred=model.predict(x_test)

# print("\n Mean Squared Error:", mean_squared_error(y_test, y_pred))

# model_poly=LinearRegression()
# model_poly.fit(x_poly_train, y_train)
# y_pred_poly=model_poly.predict(x_poly_test)

# print("\n Polynomial Mean Squared Error:", mean_squared_error(y_test, y_pred_poly))


