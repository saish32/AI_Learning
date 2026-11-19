import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder as onehotencoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


# df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# df.columns = df.columns.str.lower()
# df=df[['pclass', 'sex', 'age', 'fare', 'embarked', 'survived']]
# df.fillna({'age': df['age'].median()}, inplace=True)
# df.fillna({'embarked': df['embarked'].mode()[0]}, inplace=True)

# x=df.drop(columns=['survived'])
# y=df['survived']

# preprocessor=ColumnTransformer(transformers=[
#     ('num', StandardScaler(), ['age','fare']),
#     ('cat', onehotencoder(), ['pclass','sex','embarked'])
# ], remainder='passthrough')

# x_preprocessed=preprocessor.fit_transform(x)

# logistic_model=LogisticRegression(max_iter=200)
# log_scores=cross_val_score(logistic_model, x_preprocessed, y, cv=5, scoring='accuracy')
# print(f"Logistic Regression Cross-Validation Accuracy Scores: {log_scores.mean():.4f} ± {log_scores.std():.4f}")

# random_forest_model=RandomForestClassifier(n_estimators=100, random_state=42)
# rf_scores=cross_val_score(random_forest_model, x_preprocessed, y, cv=5, scoring='accuracy')
# print(f"Random Forest Cross-Validation Accuracy Scores: {rf_scores.mean():.4f} ± {rf_scores.std():.4f}")

# param_grid = {
#     'n_estimators': [50, 100, 200],
#     'max_depth': [None, 10, 20],
#     'min_samples_split': [2, 5, 10],
# }

# grid_search = GridSearchCV(estimator=random_forest_model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)
# grid_search.fit(x_preprocessed, y)

# print(f"Best parameters found: {grid_search.best_params_}")
# print(f"Best cross-validation accuracy: {grid_search.best_score_:.4f}")

