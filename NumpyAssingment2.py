# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 22:02:26 2017

@author: vignesht
"""

#Numpy assingment
#create 2d array using numpy
import numpy as np
a1 = np.array([[1,2,3,4],[5,6,7,8]],dtype=int)
np.shape(a1[0])
np.shape(a1[1])
np.shape(a1)

#display row sum and column sum of the matrix
print np.sum(a1,axis=0) #gives sum for row
print np.sum(a1,axis=1) #gives sum for column

#crete 3*3 matrix using arange
a2 = np.matrix(np.arange(9).reshape((3,3)));

#matrix to find out odd and even
a3 = [0,1,2,3,4,5,6,7,8,9]
a4 = []
#a4.append([0,1])
a5 =[]
for i in range(0,len(a3)):
    if(a3[i] % 2 == 0):
        a4.append(a3[i])
    else:
        a5.append(a3[i])
print a4 #prints only odd number
print a5 #prints only even number

#create 3*3 matrix and find determinent,inverse and eigen values
a5 = np.matrix(np.arange(9,18,1).reshape((3,3)))
print np.linalg.det(a5)
print np.linalg.inv(a5)
print np.linalg.eig(a5)


#demonstrate statistical function by creating 20 random values
a6 = np.random.rand(20)
np.mean(a6)
np.median(a6)
np.std(a6)
np.var(a6)
np.min(a6)
np.max(a6)
