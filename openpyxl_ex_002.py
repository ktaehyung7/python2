# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:40:02 2020

@author: nerguri
"""

from openpyxl import Workbook

write_wb = Workbook()


write_ws = write_wb.active
write_ws['A1'] = '숫자'

write_ws.append([1,2,3])
write_ws.append([4,5,6])
write_ws.cell(5,5,'5행5열')


write_wb.save("/Users/nerguri/Desktop/숫자.xlsx")