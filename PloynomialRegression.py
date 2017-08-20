# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 14:40:23 2017

@author: vignesht
"""

#Polynomial Regression

#import the packages 
import numpy as np
import pandas as ps
import matplotlib.pyplot as plt

#import the packages
dataset = ps.read_csv("Position_Salaries.csv")

#partion the depenent and independent variables for vreating a model
x = dataset.iloc[:,1:2]
y=dataset.iloc[:,-1]

#Here we have very less data so we gonna use all data for prediction 
#we can use cocept leave one out

#import sklearn and polynomial regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x,y)


#Import polynomial regression from poly regression
from sklearn.preprocessing import PolynomialFeatures
regressor1 = PolynomialFeatures(3)
x_poly=regressor1.fit_transform(x)
regressor1.fit(x_poly,y)
#For comparing create model of linear regression with same data and interpt
regressor3 = LinearRegression()
regressor3.fit(x_poly,y)

#Visualizng the data
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color = 'blue')
plt.show()
plt.title("Truth vs Bluf")
plt.xlabel("EXPERIENCE")
plt.ylabel("Salary")

#Visualize for ploy regression
plt.scatter(x,y,color='red')
plt.plot(x,regressor3.predict(regressor1.fit_transform(x)),color='blue')
plt.show()
plt.xlabel("EXPERIENCE")
plt.ylabel("Salary")

#prediction for ploy regression
regressor3.predict(regressor1.fit_transform(6.5))

#predict for linear regression
regressor.predict(6.5)