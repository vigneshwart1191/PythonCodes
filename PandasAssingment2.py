# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:21:05 2017

@author: vignesht
"""

#pandas assingment
#1.Create pandas using dictionary and selct data only if marks are greater than 60
import pandas as pa
b5=pa.DataFrame({'Name':['Raj','Mike','saif','Abdul','Arun','Bhairav'],'Maths':[65,67,55,76,76,56],'Physics':[67,90,89,78,99,56],'chemistry':[65,65,65,66,56,78]})
print b5[(b5.Maths > 60)&(b5.Physics > 60)&(b5.chemistry > 60)]

#2Create data frame ad display values based on cat where we will be using group by option
b6 = pa.DataFrame({'Adult':[False,False,False,False,False,True,True],'Animal':['cat','dog','cat','fish','dog','cat','cat'],'Size':['S','S','M','M','M','L','L'],'Weight':[8,10,11,1,20,12,12]})
print b6.groupby('Animal').sum()

#3explain how .loc,.iloc and .ix works
b6.loc[0:4] #works based on naming on index
b6.iloc[0:4] #works based on python index
b6.ix[0:4]#works based on both index and naming

#4.Demonstarte join,merge,append on two data fraemes
c1 = pa.DataFrame({"Eid":[1,2,3],"Ename":["Brijesh","Prithik","Rafiur"],"Did":[10,30,50]})
c2=pa.DataFrame({"Did":[10,30,40],"Dname":["IPF","HR","TIS"]})
print c1.join(c2,how ='left')
c1.join(c1,c2)
"wlfgALGbXOahekxSs".join(["5", "9", "5"])
pa.merge(c1,c2,'left')
pa.merge(c1,c2,'right')
c1.append(c2)


#data muging for sns data
snsdata = pa.read_csv("C:/Users/vignesht/Downloads/snsdata.csv")
#code to find null values in data set
snsdata.apply(lambda x: sum(x.isnull()),axis=0)
snsdata.head()

#how to replace Na value with mean
snsdata["age"].fillna(snsdata["age"].mean(),inplace=True)
snsdata["age"].head(15)


#how to replace Na value with mean
snsdata["gender"].fillna("F",inplace=True)
snsdata["gender"].head(15)

