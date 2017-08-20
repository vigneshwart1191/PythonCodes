# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:15:29 2017

@author: vignesht
"""

#Logstic Regression
import pandas as ps
import numpy as np
import matplotlib.pyplot as mp


#import the data set
dataset = ps.read_csv("Social_Network_Ads.csv")

#partioion independent and dependent variables
x = dataset.iloc[:,2:4]
y = dataset.iloc[:,4]

#partion data for train and test
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state = 0)

#Do feature scaling for preprocessing
from sklearn.preprocessing import MinMaxScaler
mm_s = MinMaxScaler()
x_train = mm_s.fit_transform(x_train)
x_test = mm_s.fit_transform(x_test)

#Generate a model for classification prediction
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train,y_train)

#prediction for test dataset
y_pred = classifier.predict(x_test)

#Draw confusion matrix to find the result
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)