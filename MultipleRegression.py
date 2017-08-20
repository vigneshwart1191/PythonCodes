# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 12:28:37 2017

@author: vignesht
"""

#import the librares
import numpy as np
import pandas as ps
import matplotlib.pylab as mp

#import the data set
dataset=ps.read_csv("50_Startups.csv")

#partion dependent and independent varialbel
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4]


#Create dummy variables for categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelEnocde = LabelEncoder()
x[:,3] = labelEnocde.fit_transform(x[:,3])
onehotEncode=OneHotEncoder(categorical_features=[3])
x=onehotEncode.fit_transform(x).toarray()

#remove one feature from dummy variable data so no correlation occurs b/w dummy variables
x=x[:,1:]

#partion train adn test data for generating a model
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

#Feature scaling will be done by model itself
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)


#predict the test data with model
y_pred=regressor.predict(x_test)

#import stats model for generating model and to interpt the result
import statsmodels.formula.api as sm
x=np.append(arr=np.ones((50,1),dtype=np.int),values=x,axis=1)

#created dataframe for backward propagation
x_opt=x[:,[0,1,2,3,4,5]]

#create linear regression with sm library
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

#created dataframe for backward propagation
x_opt=x[:,[0,1,3,4,5]]

#create linear regression with sm library
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

#created dataframe for backward propagation
x_opt=x[:,[0,3,4,5]]

#create linear regression with sm library
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

#created dataframe for backward propagation
x_opt=x[:,[0,3,5]]

#create linear regression with sm library
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

#created dataframe for backward propagation
x_opt=x[:,[0,3]]

#create linear regression with sm library
regressor_OLS=sm.OLS(endog=y,exog=x).fit()
regressor_OLS.summary()