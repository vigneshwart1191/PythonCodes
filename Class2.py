# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 10:07:08 2017

@author: vignesht
"""

#numpy
import numpy as nm
a1 = nm.array([[1,2,3],[4,5,6],[7,8,9]])
a1
nm.dtype
a1.dtype
a1.ndim
a1.shape #shows shape of object
a1.itemsize #shows memory size of each item in data type
a1.size
print a1[0,:]
print a1[:,:1]
print a1[:1]
print a1[:2,1:]
print a1[:,0]
print a1[1:,:2]
a1[0:][::-1]
a1[:,2]=[11,11,11]
a1

a1[:][::-1]
a1[::-1]
a1[:-1][::]

#Performing Statistical Function
a=nm.array([2,3,5],int)
a.sum()
a.prod()

nm.sum(a)

nm.mean(a)
nm.std(a)

nm.max(a)

nm.min(a)
nm.sort(a)
sorted(a,reverse=True)
#array multiplication
a3 = nm.array([[1,2,3],[4,5,6],[7,8,9]])
a4 = nm.array(a3)
a7 = a3+a4
a5 = a3*a4
a6 = a3 *5
a6
a3.dot(a4)

#matrix multiplication
a3 = nm.matrix([[1,2,3],[4,5,6],[7,8,9]])
a4 = nm.matrix(a3)
a5 = a3*a4
a7 = a3+a4
a6 = a3 *5
a6
a3.dot(a4)

#floor and celing
n1 = [2.4,6.7,8.9]
nm.floor(n1)
nm.ceil(n1)

b1 = nm.array([[1,2,3],[4,5,6]])
b2 = nm.array([[1,2,3],[4,5,6],[7,8,9]])
b2*b1
nm.dot(b1,b2)

# x + y+ z=6
# y+5z=-4
#x+5y-z=27

A=nm.array([[1,1,1],[0,1,5],[1,5,-1]])
A1=A.copy
A2=A
A1
A2

B=nm.array([[6],[-4],[27]])
AI=nm.linalg.inv(A)
x=nm.dot(AI,B)
x
x1 = nm.linalg.solve(A,B)
help(nm.linalg)
help(nm.mod)

help(nm.matrix)

help(nm.mat)
nm.m