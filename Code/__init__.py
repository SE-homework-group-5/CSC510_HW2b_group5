# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:01:36 2021

@author: anant
"""

def fibo(n):
    #This is a python code to compute the fibonacci series upto n terms
    print("Fibonacci series")
    
    a=0
    b=1
    c=0
    count=0
    fib=[]
    if n==0:
        print("n should be >0")
    elif n==1:
        print("fibonacci series of ",str(n)," terms: ",str(a) )
        fib.append(a)
    else:
        print("fibonacci series of ",str(n)," terms: ")
        while count<n:
            print(a)
            fib.append(a)
            c=a+b
            a=b
            b=c
            count+=1
            
def test_answer():
  assert len(fibo(5))==5
 
