# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:16:17 2020

@author: nerguri
"""

from openpyxl import load_workbook

load_wb = load_workbook("/Users/nerguri/Desktop/과일.xlsx", data_only=True)

load_ws = load_wb['Sheet1']

print('\n-------지정한 셀 출력-------')
get_cells = load_ws['A1':'D2']
for row in get_cells:
    for cell in row:
        print(cell.value)
        
print('\n------ 행 단위 출력 -----')
for row in load_ws.rows:
    print(row)

print('\n--- 열 단위 출력 ---')
for col in load_ws.columns:
    print(col)
        
print('\n----- 모든 행/열 출력 -----')
all_values=[]
for col in load_ws.columns:
    col_value=[]
    for cell in col:
        col_value.append(cell.value)
    all_values.append(col_value)
print(all_values)
