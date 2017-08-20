# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 14:13:48 2017

@author: vignesht
"""

################
##Assingment 2
#1.Create two dataframe and Perform all join Operation, Concatenation and Append df1 to df4
import numpy as np
import pandas as py

#Create two data frame to perfom some operations
df1 = py.DataFrame({"A":["A0","A1","A2","A3"],"B":["B0","B1","B2","B3"],"C":["C0","C1","C2","C3"],"D":["D0","D1","D2","D3"]})
df2=py.DataFrame({"B":["B2","B3","B6","B7"],"D":["D2","D3","D6","D7"],"F":["F2","F3","F6","F7"]})
#perfoming differnt joints with help of merge
py.merge(df1,df2,how='inner')
py.merge(df1,df2,how='outer')
py.merge(df1,df2,how='left')
py.merge(df1,df2,how='right')


#perform concatination operation
py.concat([df1,df2])

#perform appen operation
np.append(df1,df2)

a = [1,2,3]
a1 = len(a)
a2 = a1+1
count(a)
np.count_nonzero(a)
#3.Write a function for cumilative addition
def addition(x):
    sum = 0
    for i in range(0,len(x)):
        sum = sum+x[i]
        print sum
        #return sum
        #yield sum

addition([1,2,3,4,5])

#4.rewrite lambda into regular function
def squareValue(x):
    x = x**2
    return x
    
squareValue(4)
    

#5.find the second largest number
b1 = [ 9, 61, 2, 79, 58, 87, 68, 83, 61, 13]
b1.sort()
b1[len(b1)-2]

#6.create a matrix
a1 = np.arange(1,101).reshape((10,10))
#
#6.c
a1[4:,] #will print all values from 4th row
#with this we can come to know mean of each rows
b1= py.DataFrame(a1)
len(b1[:,1])#return number of columns
np.shape(b1)#gives number of rows and columns
b1.describe()#describes the data
#find mean of each column and row
np.mean(b1,axis=0)
np.mean(b1,axis=1)
#7create a data frame and perform some operations
df5 = py.DataFrame({"4h":[.12,.01,.03,.05],"12h":[.08,.07,.04,.09],"24h":[.06,.11,.04,.11],"48h":[.02,.09,.02,.14]},index = ["A2M","FOS","BRCA","CPOX"])
df5.index(["A2M","FOS","BRCA","CPOX"])
np.asarray(df5)#convert it into array
x1 = np.mean(df5,axis = 0)#calculate mean based on row

x2 = np.mean(df5,axis = 1)#calculate mean based on column
x3 = np.max(x2) #max value of column
x4 = py.DataFrame(x2)#
type(x2)
x4.sort(0)#sort the sum values in ascending order


    
    
    