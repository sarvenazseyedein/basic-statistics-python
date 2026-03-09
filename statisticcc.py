# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:35:57 2021

@author: Ghasemi
"""

def ave (*args):
    s=0
    m=0
    lis4=[]
    for number in args:
        lis4.append(number)
        number=s+number
        s=number
        m+=1
    print(m)
    print(number)
    mean=number/m
    print(mean)
    import xlwt
    book=xlwt.Workbook()
    sheet1=book.add_sheet("output")
    sheet1.write(0,0,"data")
    sheet1.write(1,1,mean)
    sheet1.write(0,1,"mean")
    k=0
    for n in lis4:
        k=k+1
        sheet1.write(k,0,n)
    book.save("result3.xls")  
  
"**********************************************************"
def miane (*args):
     lis=[]
     for number in args:
         print(number)
         lis.append(number)
     print(lis)
     n=len(lis)
     if n%2==0:
         medi1=lis[n//2]
         medi2=lis[n//2-1]
         median=(medi1+medi2)/2
     else:
         median=lis[n//2]
     print(median)
     import xlwt
     book=xlwt.Workbook()
     sheet1=book.add_sheet("output")
     sheet1.write(0,0,"data")
     sheet1.write(1,1,median)
     sheet1.write(0,1,"median")
     k=0
     for n in lis:
         k=k+1
         sheet1.write(k,0,n)
     book.save("result4.xls")  
 
     
"***********************************************************"
def mode (*args):
     lis=[]
     for number in args:
         print(number)
         lis.append(number)
     print(lis)
     lis1=[]
     for i in lis:
       print(lis.count(i))
       lis1.append(lis.count(i))
     print(lis1)
     num=max(lis1)
     k=lis1.index(num)
     print(lis[k])
    
     import xlwt
     book=xlwt.Workbook()
     sheet1=book.add_sheet("output")
     sheet1.write(0,0,"data")
     sheet1.write(1,1,lis[k])
     sheet1.write(0,1,"mode")
     k=0
     for n in lis:
         k=k+1
         sheet1.write(k,0,n)
     book.save("result2.xls")  
    
"***********************************************************"                 

def vari (*args):
    s=0
    m=0
    for number in args:
        number=s+number
        s=number
        m+=1
    print(m)
    print(number)
    mean=number/m
    print(mean)
    print("**********")
    lis=[]
    for number in args:
         print(number)
         lis.append(number)
    print(lis)
    print("*********")
    lis1=[]
    for j in lis:
       print(j)
       L= j-mean
       lis1.append(L)
    print(lis1)
    print("********")
    lis2=[]
    for i in lis1:
        P=i**2
        lis2.append(P)
    print(lis2)
    print(len(lis2))
    print("********")
    a=0
    for n in lis2:
         n=n+a
         a=n
    print(n/len(lis2))
    import math 
    meyar= math.sqrt(n/len(lis2))
    print(meyar)
    
    import xlwt
    book=xlwt.Workbook()
    sheet1=book.add_sheet("output")
    sheet1.write(0,0,"data")
    sheet1.write(1,1,n/len(lis2))
    sheet1.write(0,1,"var")
    sheet1.write(0,2,"meyar")
    sheet1.write(1,2,meyar)
    k=0
    for n in lis:
         k=k+1
         sheet1.write(k,0,n)
    book.save("result1.xls")
         
      
             
        
       
        
      
    
    
   

  
    
    
    