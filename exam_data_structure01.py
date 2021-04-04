# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:27:56 2019

@author: nerguri
"""

"""
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#print(fruits.count('apple'))
#print(fruits.index('banana', 5))
fruits.reverse()
fruits.append('grape')
fruits.sort()
print(fruits.pop())
print(fruits.pop())
"""

"""
stack = [1,2,3,4,5]
stack.append(6)
stack.append(7)
print(stack.pop())
print(stack.pop())
"""

"""
from collections import deque
queue = deque(["Eric", "John", "Michele"])
queue.append("Terry")
queue.append("Graham")
print(queue)
"""

"""
squares = [x**2 for x in range(10)]
  
print(squares)
"""

"""
vec=[[1,2,3],[4,5,6],[7,8,9],[10,11,13]]
a = [num for elem in vec for num in elem]
print(a)
"""

"""
t=[]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#for i in range(4):
#    t.append([row[i] for row in matrix])
print(list(zip(*matrix)))
"""

"""
a=[1,]
t = 12345, 54321, 'hello!'
u = t, (1,2,3,4,5)
print(u)
empty=()
singleton = 'hello',
print(singleton)
t = 12345, 54321, 'hello!'
x,y,z=t
"""


"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)

a = set('abracadabra')
print(a)
b = set('alacazam')
print(b)
print("a-b: ", a-b)
print("a|b: ", a|b)
print("a&b: ", a&b)
print("a^b: ", a^b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a.)
"""

"""
tel={'jack':4098, 'sape':4139}
tel['guido']=4127

print(tel)
print(tel['jack'])
del tel['sape']
tel['irv']=4127
print(tel)
a=sorted(tel)
"""

"""
a = dict([('sape', 4139), ('guido',4127), ('jack',4098)])
b = {x:x**2 for x in (2,4,6)}
c = dict(sape=4139, guido=4127, jack=4098)
"""

"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k, v)

for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q,a))

for i in reversed(range(1,-10,-2)):
    print(i)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in reversed(set(basket)):
    print(f)
"""

"""
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data =[]
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
"""

"""
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
"""























