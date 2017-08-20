# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:00:34 2017

@author: vignesht
"""

#Basic programming 
#1.orint data which is less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,4]
for i in range(1,len(a)):
    if(a[i] < 5):
        print a[i]
##print values which is less than 5 and store it in another list
a1=[]
for i in range(1,len(a)):
    if(a[i] < 5):
        a1.append(a[i])

print a1

###write this in one line of python
#with user input enter number
a5=[]
a2 = raw_input()
v1 = int(a2)
for i in range(1,len(a)):
    if(a[i] < v1):
        a5.append(a[i])

print a5

#slice values of 20 and 25
a6 = [5, 10, 15, 20, 25, 30, 35, 40] 
a6[3:5]


#write program for fibonnaci series and seperate by commas
value=1000
n1=0
n2=1
print n1
print n2
for i in range(2,value):
    n3=n1+n2
    if(n3 > 1000):
        break
    else:
        print n3
        print ','
    n1=n2
    n2=n3
    

#get a raw input from user and calulate their age
name = raw_input()
a10 = raw_input()
age = int(a10)
estimate = 100-age
print "Number of years it will take take for you to reach 100:",estimate 
    
    
#sum numbers which is odd
import numpy as np
z1 = np.arange(0,100)
sum=0
for i in range(0,100):
    if(z1[i] % 2 != 0):
        sum+=z1[i]
        
print sum


#palindrom of string
#a = "HelloWorld"
a=raw_input()
b=[]
c = list(a)
for i in range(1,len(c)):
   b.append(c[-i]) 
b.append(c[0])

if(c == b):
    print "This string is a palindrome"
else:
    print "String is not a palindrome"
    
    
#7create a string and conert to upper case and print in reverse order
u1 = "GIS Programming" 
u2 = u1.upper()
u3 = list(u2)
u4=[]
print len(u3)
for i in range(1,len(u3)):
    u4.append(u3[-i])
u4.append(u3[0])

print u4