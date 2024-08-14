# -*- coding: utf-8 -*-
"""Model Evaluation:Train, TestSplit

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JSZPy-86XiJDJeXMytvXbsntHk8awzeT
"""

import pandas as pd
url= "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"

column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']

df=pd.read_csv(url, delim_whitespace=True, names=column_names, na_values='?', comment='\t')

df.head()

df.isna().sum()

df.horsepower.describe()

df['horsepower'].fillna(df.horsepower.mean(), inplace=True)
df.isna().sum()

Features = [ 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin']
x = df[Features]
y= df['mpg']

y

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x.shape

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

x_train

x_train.shape

x_test.shape

80/398

model=LinearRegression()
model.fit(x_train, y_train)

"""model evaluation metrix"""

y_pred = model.predict(x_test)
y_pred[:5]

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
mse

r2_score(y_test, y_pred)

"""r2 score: help to compare
we take differen
if difference is -ve then its bad

"""

model.score(x_test, y_test)