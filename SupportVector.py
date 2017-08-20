# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:58:53 2017

@author: vignesht
"""

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

#Feature scALING NEED TO BE DONE SO SVR MODEL DOSENT NORMALIZE DATA BY ITSELF
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
sc_y=StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)
#import sklearn and polynomial regression
from sklearn.svm import SVR
regressor = SVR()
regressor.fit(x,y)

#prediction for ploy regression
y_pred = sc_y.inverse_transform(regressor.predict(sc_x.fit_transform(np.array([[6.5]]))))

#Visualize for ploy regression
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.show()
plt.xlabel("EXPERIENCE")
plt.ylabel("Salary")



