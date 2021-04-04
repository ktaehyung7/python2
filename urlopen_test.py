# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:39:43 2019

@author: nerguri
"""
from urllib.request import urlopen

with urlopen('http://www.naver.com') as response:
  for line in response:
    line=line.decode('utf-8')
    if 'code' in line:
      print(line)