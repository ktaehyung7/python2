# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:26:33 2020

@author: nerguri
"""

import pandas as pd
import numpy as np
import matplotlib as plt

pd.set_option('display.expand_frame_repr', False)

a = [0]

# adjustment value
adjust_amt = 0.25
adjust_diff = 0.30

# prediction duration
prediction_duration = 5


df8 = pd.read_csv('C:/Users/nerguri/Desktop/095700_test.csv', sep=',', encoding='EUC-KR', index_col='일자')

df8 = df8.sort_index(axis=0, ascending=True)

for value in range(len(df8)):
    if value == 0:
        continue
    a_dif = df8.iloc[value].종가 - df8.iloc[value-1].종가
    a.append(a_dif)

df8['대비'] = a