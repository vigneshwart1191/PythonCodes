# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:02:40 2017

@author: vignesht
"""

#Scipy Tutorial
#scipy is a scientific python
#open source
#Ex:Image processing
#build above numpy
#to install pip pakage pip insttal package
import scipy as si
from scipy import stats#importig sub packages
dir(stats)#SHOWS HOW MANY FUNCTIONS THERE IN STATS SUB PACKAGE


#random number generation using scipy
s = si.rand(100)
s.min()
s.max()
s.mean()
s.std()
s.var()
s1 = stats.describe(s)
n,min_max,mean,var,skw,kur=stats.describe(s)
#can acess through index
s1[1][1]

#scipy intergration
from scipy.integrate import quad
i=si.integrate.quad(lambda x:si.special.jv(2.5,x),0,4.5)

#Linear Equation
from math import *
I = sqrt(2/pi)*((18/27)*sqrt(2)*cos(4.5))-((4/27)*sqrt(2)*sin(4.5))+(sqrt(2*pi)*si.special.fresnel(3/sqrt(pi)))

#linear algebra
A = si.mat('[1 10 7;2 4 2;9 2 8]')
B=si.mat('[12;7;8]')
si.linalg.solve(A,B)
si.linalg.det(A)


#files whic we can used to read and write data
f = open('C:/Users/vignesht/Desktop/HadoopAssignment.docx','rU')
for line in f:
    print line
    
f.close()
#'w' for write and 'a' for append
#write a file
import csv
with open(')

#os operations
import os as os
os.listdir('C:/Users/vignesht/Desktop')#shows all files in the directary
os.path.join('C:/Users/vignesht/Desktop/sample1')

import urllib2
f = urllib2.urlopen('http://www.cricbuzz.com')
print f.read(1000)

#downloading image in python
from urllib import *
urlretrieve("https://www.google.co.in/imgres?imgurl=https%3A%2F%2Faos.iacpublishinglabs.com%2Fquestion%2Faq%2F1400px-788px%2Fpandas-live_64dff22c2fe56e9.jpg%3Fdomain%3Dcx.aos.ask.com&imgrefurl=https%3A%2F%2Fwww.reference.com%2Fpets-animals%2Fpandas-live-64dff22c2fe56e9&docid=vIExH1naZyGyZM&tbnid=WyKT0k7c_xB4PM%3A&vet=1&w=1400&h=788&bih=602&biw=1242&q=panda&ved=0ahUKEwiemOPJwIzSAhXKs48KHfYjBd4QMwg4KAEwAQ&iact=mrc&uact=8",'tug.png')


#



