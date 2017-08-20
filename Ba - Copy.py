# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:13:20 2017

@author: vignesht
"""

a=5
b=5
c=5
if(a=b and a=c):
	print "equilateral triangle"
elseif(a=b or a=c or b=c):
	print "Isosceles triangle
elseif(a^2 +b^2 = c^2 or  c^2+b^2 = a^2 or a^2 + c^2= b^2):
	print "Right angle traingle"
else:
	print "Scalene triangle"