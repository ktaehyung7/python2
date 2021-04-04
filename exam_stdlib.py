# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:23:50 2019

@author: nerguri
"""

"""
import os

print(os.getcwd())

os.chdir('./db')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.system('mkdir db2')
"""


#print(dir(os))
#print(help(os))

"""
import shutil
#shutil.copyfile('sample.dat','aaa.dat')
shutil.move('aaa.dat', 'bb.dat')
"""

"""
import glob
a=glob.glob('*.py')
print(a)
"""

"""
import sys
print(sys.argv)
"""

"""
import argparse
from getpass import getuser

parser = argparse.ArgumentParser(description='An argparse example.')
parser.add_argument('name', nargs='?', default=getuser(), help='The name of someone to greet.')
parser.add_argument('--verbose', '-v', action='count')
args=parser.parse_args()
greeting = ["Hi", "Hello", "Greetings! its very nice to meet you"][args.verbose % 3]
print(f'{greeting}, {args.name}')

if not args.verbose:
    print('Try running this again with multiple "-v" flags!')
"""

"""
import re

a=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

print(a)

b=re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

print(b)
"""

"""
a='tea for too'.replace('too', 'two')
print(a)
"""

import math
a=math.cos(math.pi/4)
print(a)






























