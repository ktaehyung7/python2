# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:52:36 2019

@author: nerguri
"""

"""
try: 
    x = int(input("Please enter a number: "))
    print(x)
except ValueError:
    print("!! syntax err !!")
""" 
   
""" 
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
"""


"""
try:
     raise Exception('spam', 'raised spam exception')
except Exception as inst:
     print(':::{}'.format(inst))
     print(type(inst))    # the exception instance
     print(inst.args)     # arguments stored in .args
     print(inst)          # __str__ allows args to be printed directly,
                          # but may be overridden in exception subclasses
     x, y = inst.args     # unpack args
     print('x =', x)
     print('y =', y)
"""















































