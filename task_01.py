# -*- coding: utf-8 -*-
"""Task-01

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15ZT6er_EhxY8muFi9vbBjKBNCCfmkQbw
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Loading the dataset
data=pd.read_csv('/content/Housing.csv')
df=pd.DataFrame(data)

# Selecting the features and target variable
df.replace(('yes','no'),(1,0),inplace=True)
df.replace(('furnished','semi-furnished','unfurnished'),(2,1,0),inplace=True)
x=df.iloc[ : , :-1].values
y=df.iloc[ : ,0:1].values

# We will perform the data splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

# instance of the Linear Regression model creation
model = LinearRegression()

# Training the model
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating the model
score = model.score(X_test, y_test)
print("Model R^2 Score:", score)
# Predicting the price of a new house
new_house = pd.DataFrame({'area':[7420],'bedrooms': [4], 'bathrooms': [2]})
predicted_price = model.predict(new_house)
print("Predicted Price:", predicted_price[0])