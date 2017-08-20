# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:18:59 2017

@author: vignesht
"""

#Apriori Algorithm
#For this need to have apyori function code can be taken from python

#import the packages
import numpy as np
import pandas as pa
import matplotlib.pyplot as py

#import the datset
dataset = pa.read_csv("Market_Basket_Optimisation.csv",header = None)

#Apriori algorith will take data as list only so conver dataframe into list
transacions = []
for i in range(0,7501):
    transacions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
    
#Generate a apriori algorithm for associate rules
from apyori import apriori
rules = apriori(transacions,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2)

#Form a rules
results = list(rules)