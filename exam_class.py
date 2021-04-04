# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:16:24 2019

@author: nerguri
"""

"""
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
"""

"""
class MyClass:
    i=12_345
    
    def f(self):
        return 'hello world'
    
    def g(self):
        return self.i
    
x=MyClass()
print(x.i)
print(x.f())
print(x.g())
"""

"""
class Complex:
    def __init__(self, a,b):
        self.a = a
        self.b = b
        
x=Complex(1,2)

x.counter = 1
while x.counter <10:
    x.counter *= 2
    
print(x.counter)
del x.counter
"""

"""
class Dog:
        
    def __init__(self, name):
        self.name = name
        self.tricks = []
        
    def add_trick(self, trick):
        self.tricks.append(trick)
        
d=Dog('Fido')
e=Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play alive')

print(d.tricks)
print(e.tricks)
"""

"""
def f1(self, x, y):
    return min(x, x+y)

class C:
    f=f1
    
    def g(self):
        return 'hw'
    
    h=g
    
x=C()
print(x.f(1,-5))
print(x.g())
print(x.h())
"""

"""
class Bag:
    def __init__(self):
        self.data=[]
        
    def add(self, x):
        self.data.append(x)
        
    def addtwice(self, x):
        self.add(x)
        self.add(x)
        
x=Bag()
x.add(1)
print(x.data)
x.addtwice(20)
print(x.data)
"""

"""
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MSubClass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
            
x=MSubClass('1')

print(x.items_list)
"""

"""
class Employee:
    pass

john = Employee()

john.name = 'john doe'
john.dept = 'com lab'
john.salary = 1_000_000
"""

"""
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for value in {'one':1, 'two':2}:
    print(value)
for i in range(123):
    print(i)
"""

"""
s='abc'
it=iter(s)
li=list(it)
print(li)
"""

"""
class Reverse:
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev=Reverse('spam')
it=iter(rev)
#print(next(it))
#print(next(it))

for char in rev:
    print(char)
"""

"""
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
for char in reverse('golf'):
    print(char)
"""

"""
print(sum(i*i for i in range(10)))

xvec = [10,20,30]
yvec = [7,5,3]
print(sum(x*y for x,y in zip(xvec, yvec)))

zvec = xvec + yvec
a = set(zvec)
print(a)
b = list(a)
print(b)
"""

"""
x = [[1,2,3],[4,5,6],[7,8,9]]


for i in range(3):
    for j in range(3):
        print(x[i][j],end='')
    print('')
   """ 

















