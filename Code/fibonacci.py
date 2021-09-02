# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:01:36 2021

@author: anant
"""
#This is a python code to compute the fibonacci series upto n terms
print("Fibonacci series")

#taking input of number of terms
n=int(input("Enter Nbr of Terms: "))

a=0
b=1
c=0
count=0
if n==0:
    print("n should be >0")
elif n==1:
    print("fibonacci series of ",str(n)," terms: ",str(a) )
else:
    print("fibonacci series of ",str(n)," terms: ")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
