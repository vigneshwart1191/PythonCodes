# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:51:27 2017

@author: vignesht
"""

#scipy assingment
import pandas as ps
import scipy as sp
a2 = sp.matrix('[2 3 4;7 6 5;1 2 3]')
sp.linalg.det(a2)

#2.Take 3*3 matrix and perform slicing operations
import numpy as np
a3 = sp.array([[1,2,3],[4,5,6],[7,8,9]])
a4 = sp.matrix(a3)
print a4[1:3,0:3] #prints 2nd row and 3rd row
print a4[0:3,1] #prints second column
a4[0,0:3]=[1,2,3] #replace old values with new values


#3.Demonstrate statistical function using scipy
a1 = [1,2,3,4,5,6,7,8,9,10]
sp.mean(a1) #calculates mean
sp.std(a1) #calculates standard deviation
sp.var(a1) #calculate variance
sp.amax(a1) #calculate min value
sp.amin(a1) #return max value
a2 = sp.histogram(a1) #will give frequency distribution
sp.median(a1) #will give median value

#4.
from scipy.integrate import quad
i=sp.integrate.quad(lambda x:si.special.jv(2.5,x),0,4.5)

#5.solve linear algebra question
#linear algebra
A = sp.mat('[1 -2 3;2 3 1;-4 0 1]')
B=sp.mat('[3;6;9]')
sp.linalg.solve(A,B)
sp.linalg.det(A)


#extract age through date time library
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

calculate_age('11-09-1991')

#6.download some image from url
import urllib

urllib.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg",'C:/Users/vignesht/viggy.jpg')

#7.