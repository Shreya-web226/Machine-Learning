# -*- coding: utf-8 -*-
"""polynomial Regression

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h2JWQmlj6UPM6JgER6I0iLpTXvC38_Ta
"""

import pandas as pd
import numpy as np

df=pd.read_csv("/content/car_prices.csv")
df.head()

from matplotlib import pyplot as plt
plt.figure(figsize=(8,6))
plt.scatter(df.mileage,	df.selling_price)
plt.show()

from sklearn.model_selection import train_test_split

X = df[['mileage']]
y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

X.shape, X_test.shape

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
poly.fit_transform(np.array([[1],[2],[3],[4]]))

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_train_poly = poly.transform(X_test)

X_train_poly[:5]

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

model = LinearRegression()
model.fit(X_train_poly, y_train)

y_pred = model.predict(X_test_poly)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mse, r2

x_range = np.linspace(X['mileage'].min(), X['mileage'].max(), 300).reshape(-1, 1)
x_range_poly = poly.transform(x_range)
y_range_pred = model.predict(x_range_poly)

plt.scatter(X_test['mileage'], y_test, label='Actual Data')
plt.plot(x_range, y_range_pred, color='orange', label='Polynomial Regression Line')
plt.title('Used Car Pricing: Polynomial Regression Fit')
plt.xlabel('Mileage')
plt.ylabel('Selling Price')
plt.legend()
plt.show()