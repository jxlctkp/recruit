#!/usr/bin/python

def fib(n):
    a,b=0,1
    result=[]
    while(a<n):
      result.append(a)
      a=b
      b=a+b
    return result

arrlist_fib=fib(200)
print arrlist_fib
      
    
      
