# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:01:44 2017

@author: vignesht
"""

#class4
#Padas
#pandas is used to perform data frame in r
import pandas as py
import numpy as np
#two data structures in pandas
    #1.series->1-d array ,2.dataframe->2-d array

#series usage and can be passed in all list,tuple and dataframe
s = [1,2,3,4,5]
i = ['a','b','c','d','e']
s1 = py.Series(s,index = i)
s2 = (1,2,3,4,5)
s3=py.Series(s2)
s4 = {"Z":"1","Name":"Vigneshwar","Lname":"Thiyagarajan","Age":20}
s5 = py.Series(s4)
s6= ['b','c','a']
s7 = py.Series(s6)

#dataframe
s = [1,2,3,4]
i = ['a','b','d','e']

s5 = py.DataFrame(s,i)
s5['age'] = 20
s5.columns=['num','char']

#data frame
df = pa.DataFrame({'A':[1,2,3,4],'b':[10,20,30,40],'c':[-1,-2,-3,-4]})
df
df.index = ['a','b','c','d']

#date which is known as time series
dates = py.date_range('20170101',periods = 10,freq = 'M')
df1 = py.DataFrame(np.random.randn(10,4),index=dates,columns=list('ABCD'))
df1.head(n=2)
df1.tail(n=2)
df1.describe()
df1[1:3]
df.loc[0:2] #deals with label indexes
df.iloc[0:2] #iloc deals with python indexes
df.ix[0:2,0:2] #deals with lables which takes upto lables


#group by columns
df2 = py.DataFrame({'A':[1,1,1,2,2,2,3,3,4,5,5,5],'B':[1,2,3,4,5,6,7,8,9,10,11,12]})
df2.groupby('A').sum()

#import csv files
glass = py.read_csv('C:/Users/vignesht/Downloads/glass.csv')

import html5lib as ht
#import html file
html1 = py.read_html('http://www.w3schools.com/html/html_tables.asp')



#class5
df3 = py.DataFrame({"Paris":[0,3,6],"Berlin":[1,7,4],"Madrid":[2,5,8]})
df3.index = ['a','b','c']

#slicing data through ix
df3.ix[0:2,0:2]
df3.ix[:,"Berlin"]
df3.ix["a",:]
df3.loc["a",:]
df3.iloc[0:2,0:2]
#sorting based on index
df3.sort_index(by='Madrid')
df3.sort_index(axis = 0,ascending = False)
df3.sort_index(axis = 1,ascending = False)
df3.drop("Berlin",axis = 1)


#Compuing statistics
df3.describe() #to summarize the data
df3.corr()  #to find correlation
df3.T  #transpose rows into columns
df3.cov()#covariance

import math
#apply map usage  
f = lambda x:np.sqrt(x)
df3.applymap(f)
df3.Berlin = df3['Berlin'].map(f)


#concatination on series
s1=py.Series(np.arange(0,3))
s2 = py.Series(np.arange(4,7))
s3 = py.concat([s1,s2],1)
s3.index = ["a","b","c","d","e","f"]
type(s3)

type(np.arange(1,4))
type(range(1,4))


######################
###Data Munging
data = [1,2, ,3, ,4]
data.isnull()


















