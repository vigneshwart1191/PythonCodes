# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 10:15:16 2017

@author: vignesht
"""
#addition
x = 1+2**3/4*5
#divison of float
y  = 3.0/2
#data type of value0
type(y)
#type conversion
f = int(y)
type(f)
#perfoming string with error
n=("123")
n1 = 5
n3 = int(n)
n2 = n1+n3
print(n2)

#addition of two numbers explicitly
num1 = input("Enter no1:")
num2 = input("Enter no 2:")
num3 = num1+num2
num3
type(num3)

#string methods
a = "this is is a good"
a.count("is")
a.capitalize()
a.center(30)
c = a.encode
c
d = c.decode
d

#string an array
a = "Hello"
a[1:3]
a[1:]
a[:]
a[-3:]
a[-4:-1]
a[1:-3]

#3 numbers
def bnumber(a1,a2,a3):
    if(a1>a2 and a1>a3):
        print("A1 Value is biggest of three numbers")
    elif(a2>a1 and a2>a3):
        print("A2 Value is biggest of three numbers")
    else:
        print("A3 Value is biggest of three numbers")
        
bnumber(45,65,76)



#factorail of number
def factnumber(x):

    if(x<0):
        print "Not eligible for factorial"
    elif(x == 0):
        print 1
    else:
        fact=1
        i = 1
        while(i <= x):
            fact = fact*i
            i=i+1
    return fact
    
print factnumber(5)

#range example
r = range(1,10)
type(r)
 
 #for example
 for i in range(1,20,2):
     print i 
#in example which returns true or false
 3 in r
    
#if in example which returns boolean value and can give condition
if 3 in r:
    print "Great Bhairav jain"
    
    
#example of list operations in append and extend
list = [1,2,34,5,6]
1 in list #checks in list and return true or false
list.append(55) #insert value at last
list.extend([7,8,9]) #will take in list to insert values in list
list.extend([10])
list.insert(3,0) #based on index values will be inserted
list.pop(3) #remove last value or else based on index it will remove
list.remove(2) #remove values based on values in list


#sorting
print sorted(list,reverse = True)
print sorted(list,reverse = False)

#tuple
tuple1 = (1,2,3,45)
#its imutable

#dictionary
b1 = {"Fname":"Vigneshwar","Lname":"Thiyagarajan"}
b1["Fname"]="Viggy"
b1.pop("Viggy")
del b1["Fname"]
b1["Firstname"] = b1.pop("Fname")#its mutable 


#inbuild function
a3 = 12345
print bin(a3)
print oct(a3)
print hex(a3)


#lamda function
a = lambda x,y:x+y
c = a(2,3)

#celcius to farenheit
celcius = [28,29,34.34,32,63]
#map function
f = map(lambda x:(float(9)/5)*x+32,celcius)
f

#reduce function
ce = [1,2,3,4,5]
f1 = reduce(lambda x,y:x+y,ce)
f1


#filter
fi1 = filter(lambda x:x==2,ce)
fi1