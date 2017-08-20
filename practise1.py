# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 23:46:15 2017

@author: vignesht
"""

#1.factorial of n numbers
n=5
sum = 1
for i in range(1,n+1):
    sum =sum*i
    
sum

#2.fibonnaci
n1=0
n2=1
cal = 10
print n1
print n2
for i in range(2,cal):
    n3=n1+n2
    print n3
    n1=n2
    n2=n3

#reverse a number
number = 123
n1=0
while(number > 0 ):
    n=number%10
    n1=(n1*10)+n
    number=number//10

#
#
import numpy as np
import pylab as py
x=[1,2,3,4,5]
y=[12,14,2,16,3]
x1=py.plot(x,y)
py.show(x1)
help(py.plot)

#plot
x2 = np.random.rand(100)
py.plot(x2)
x3=np.random.randn(100)
py.plot(x4)
x4 = x3.py.hist
x4
x=np.linspace(-np.pi,np.pi,256,endpoint = True)
c=np.cos(x)
s=np.sin(x)
t=np.tan(x)
py.plot(x,s)
py.plot(x,c)
help(np.linspace)
help(py.plot)

#histogram
py.hist(np.random.randn(100))
import matplotlib.pyplot as ml
#histogram
data = np.random.randn(100)
f,(ax1,ax2) = ml.subplots(1,2,figsize=(6,3))
ax1.hist(data,bins=30,normed=True,color = 'b')
ax2.hist(data,bins=30,color='r')

#subplots
a = [1,2,3,4,5]
b = [6,7,8,9,1]
py.subplot(1,1,1)
py.plot(a)
py.subplot(2,1,1)
py.plot(b)

