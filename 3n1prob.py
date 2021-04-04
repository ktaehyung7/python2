# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:00:16 2019

@author: nerguri
"""

def cypro(k):
    cl=1
    while k != 1:
        if k%2==0:
            k /=2
            cl +=1
        else:
            k=3*k+1
            cl +=1
    return cl

i=int(input('input min num: '))
j=int(input('input max num: '))
t=0
arw=[]

for t in range(i, j+1):
    arw.append(cypro(t))
print(arw)
print(max(arw))