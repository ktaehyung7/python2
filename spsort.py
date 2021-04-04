# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:40:56 2019

@author: nerguri
"""

a=[-1,1,3,-2,2]
def _swap(k):
    temp=a[k]
    a[k]=a[k+1]
    a[k+1]=temp

for i in range(len(a)): 
    for j in range(len(a)-1): 
        if a[j] > 0 and a[j+1] < 0: 
            _swap(j)