# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:10:59 2019

@author: nerguri
"""

"""
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
"""

"""
yes_votes=42_572_654
no_votes=43_132_495
percentage = yes_votes / (yes_votes+no_votes)
print('{:-9} YES votes, {:2.2%}'.format(yes_votes, percentage))
"""

"""
s='Hello, world.'
str(s)
repr(s)

s=str(1/7)
print(s)

x=10*3.25
y=200*200
s='THe value of x is '+repr(x) + ', and y is ' + repr(y) +'...'
print(s)

hello='hello, world\n'
hellos=repr(hello)
print(hellos)

r=repr((x,y,('spam', 'eggs')))
r=(x,y,('spam', 'eggs'))
print(r)
"""
"""
import math
print(f'The value of pi is approximately {math.pi:.6f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
    print(f'{name:10} ===> {phone:10d}')
    
a = 'eels'
print(f'{a!r}')
"""

"""
print('We are the {} who say "{}!"'.format('knights', 'Ni'))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('{[Jack]}'.format(table))

s = '4321'
print(s[0])
"""

"""
for x in range(1,3):
    print(repr(x).ljust(3), repr(x*x).rjust(5), end=' ')
    print(repr(x*x*x).rjust(4))
    
print('12'.zfill(5))    
"""

"""
import math
print('value: %5.3f, %2d'% (math.pi , 3))
"""
"""
with open('sample.dat', 'w') as f:
    f.write('파일에 기록될 문자열입니다.\n')
    f.write('파일 기록하는거 참 쉽죠?!\n')
    f.close()
"""

"""
with open('sample.dat', 'r') as f:
    a = f.read()
    f.close()
    word=a.split('\n')
    x=word[0].split(' ')
    print('%d  %d'%(int(x[0]), int(x[1])))
"""


        


    


















