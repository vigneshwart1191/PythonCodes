# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 12:16:27 2017

@author: vignesht
"""

###loan data
import pandas as py

######imported the data set
loanData = py.read_csv("C:/Users/vignesht/Downloads/train.csv")


#preporccesing hte data
##find the missing values in data set
sum(loanData.isnull())
loanData.describe()
#code to find null values in data set
loanData.apply(lambda x: sum(x.isnull()),axis = 0)
loanData.head()

#how to replace Na value with mean
loanData["LoanAmount"].fillna(loanData["LoanAmount"].mean(),inplace=True)
loanData["LoanAmount"].head(15)


#to find factors and number of values in factor data


#replace Factor dataloanData["Gender"].value_counts()
loanData["Gender"].fillna("Male",inplace=True)
loanData["Gender"]


###for log transformation
loanData['LoanAmount_Log']=np.log(loanData['LoanAmount'])
loanData['LoanAmount_Log'].hist(bins = 10)