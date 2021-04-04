# -*- coding: utf-8 -*-
"""
Created on Fri May 10 07:57:31 2019

@author: nerguri
"""

import tensorflow as tf
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

df8 = pd.read_csv('C:/Users/nerguri/Desktop/043090_csv.csv', sep=',', encoding='EUC-KR', index_col='dates')

df8_r = df8[-4:]