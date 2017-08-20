# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 15:43:02 2017

@author: vignesht
"""

##1.What is 7 to the power of 4?

x = 7**4
print(x)

##2.Split this string:"Hi there Sam!"
s = "Hi there Sam!"
b = s.split()
print(b)


#3.create a string and returns true if word is there in string
def fstring(a1):
    str1 = "dog"
    print(str1 in a1)
    
    
fstring('Is there a dog here?')


#4.create a function to count dog in string
def fstring1(a2):
    str2 = 'dog'
    print a2.count(str2)
    
fstring1('This dog runs faster than the other dog dude!')

#5.hig speed police problem
def speed(s,b):
    if(s<60 and b == 0):
        print("No ticket")
    elif(s<65 and b == 1):
        print("No Ticket")
    elif(s>61 and s<81 and b == 0):
        print("small ticket")
    elif(s>61 and s<86 and b == 1):
        print("small ticket")
    elif(s>81 and b == 0):
        print("big ticket")
    else:
        print("big Ticket")
       
speed(65,1)
speed(76,0)
speed(84,1)
speed(90,1)


#6 . use lamda function and fliter values in list
my_list = ['soup','dog','salad','cat','great']
new_list = list(filter(lambda x: x.find("s") , my_list))
print(new_list)


#7.write a code in list to create rainbow colors
list1 = ["Violet","red","orange","yellow","green","blue","indigo"]
print(list1)

#8.write a code to add two strings
str2 = "abc"
str3 = "def"
#method 1 to use +sign
str4 = str2+str3
#use concat method
str5 = ("ab","bc")
print str2.join(str5)
print(str4)


#9.easiet way print same string 10 times
str7 = "abc"
str7*10

#10. write a code to add new elements in list
aList = [123, 'xyz', 'zara', 'abc'];
aList.append( 2009 );
print "Updated List : ", aList


#11 celcius to Fahrenheit 
c=37.5
print (lambda f : (c * 1.8) + 32)



#12.code for odd or even
def oddeven(x):
    if(x % 2 == 0):
        print("Even number" , x)
    else:
        print("odd number" , x)
        
oddeven(7)
        

#13.remove 4th element in the list
aList = [123, 'xyz', 'zara', 'abc'];
aList.remove(aList[3])
print(aList)

#14.insert element in 6th position
l8 = [1,2,3,4,5,6,7,8,9]
l8.insert(5,56)
print l8


#15 Identify the following data types
A = (1, 2, 3) #tuple
B = [1,2,3] #list

#C = {‘Name’: ‘Saikat’, ‘Age’:49} #dictionary which has key and value


#16write code to print 1 to 100 using range
for i in range(1,101):
    print(i)
    

#17 write code to sort list
list1=[10,50,13,'rahul','aakash']  
list1.sort()  
print list1  


#18.which of the list immutable
##tuple is the list which is immutable 

#19How to delete all contents i dictionary
dict1 = {"Fname" : "Vigneshwar","Lname" : "Thiyagarajan" , "Age" : "21"}
del dict1

#20 code to display largest of three numbers
def bnumber(a1,a2,a3):
    if(a1>a2 and a1>a3):
        print("A1 Value is biggest of three numbers")
    elif(a2>a1 and a2>a3):
        print("A2 Value is biggest of three numbers")
    else:
        print("A3 Value is biggest of three numbers")
        
bnumber(45,65,76)