# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 21:56:15 2017

@author: vignesht
"""
#1
x = 3
type(x)

#2
x1=[1,2,3,4]
type(x1)
x1.insert()

x2 = 1.2
type(x2)

x3 = (2,3,4,5)
type(x3)
x3.insert(6)

#3
a1 = True
a2 = False
a1 and a2
not a1
a1 != a2

#4
b1 = 'Hello'
b2 = "World"
print 'abc'
print b1+" "+b2
b1.capitalize()
b1.upper()
b1.decode()
b1.endswith("1")
b1.find("l")
b1.rjust(10)
b1.center(20)
b1.replace("l","1234"[3])

#5
c1 = [1,2,3,4]
c1.append([5,6,7,8])
c1.pop(1)
c1[0]="Hello"
c1[-3]
c1[:2]
c1[2:4]
c1[1:]
c1[-1:]
c1[-0:-2]
c1[-1:-0]
c1[-2]
len(c1)
shape(c1)
c1.shape()
#6
d1 = range(1,100)
for i in enumerate(d1):
    print i

#list
c2 = []
for a in c1:
    c2.append(a**2)
    
print(c2)

#7
d1 = {'Virat':'Kholi',"MS":"Dhoni","Ab":"Dev"}
d1['Virat']
d1['Kholi']#throws error
d1["Yuvi"]="Singh"
d1[1]#throws error when trying to acces through index for dictionary
del d1['Virat']
d1.get("MS")

#8Numpy package working and function
import numpy as np
e1 = np.array([1,2,3])
type(e1)
e1.shape()
np.shape(e1)
np.rank(e1)
e2 =np.array( [[1,2,3],[4,5,6]])
np.shape(e2)
print e2[0,1],e2[0,2]
type(e2)
np.rank(e2)
type(e2)