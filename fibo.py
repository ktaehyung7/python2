# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:14:30 2019

@author: nerguri
"""
import sys

def fib(n):
    a, b=0,1
    while a < n:
        print(a,end=' ')
        a, b = b, a+b
    print()
    
def fib2(n):
    result=[]
    a, b=0,1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def main():
    fib(int(sys.argv[1]))
    
if __name__ == "__main__":
    main()