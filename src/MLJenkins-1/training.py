import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/house_price.csv")
x = df.drop('price', axis=1)
y = df['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=33)

lr = LinearRegression()
lr.fit(x_train, y_train)


# os.makedirs("model", exist_ok=True)  # succeeds even if directory exists.
joblib.dump(lr, 'model/model.pkl')

print(lr.score(x_test, y_test))