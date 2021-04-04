# -*- coding: utf-8 -*-
"""
Created on Wed May 16 08:20:23 2018

@author: nerguri
"""

import pandas as pd
import numpy as np
import matplotlib as plt


pd.set_option('display.expand_frame_repr', False)

# adjustment value
adjust_amt = 0.10
adjust_diff = 0.30

#메리츠
#df8 = pd.read_csv('C:/Users/nerguri/Desktop/008560_csv.csv', sep=',', encoding='EUC-KR', index_col='dates')
#제넥신
#df8 = pd.read_csv('C:/Users/nerguri/Desktop/095700_csv.csv', sep=',', encoding='EUC-KR', index_col='dates')
#팜스웰바이오
df8 = pd.read_csv('C:/Users/nerguri/Desktop/043090_csv.csv', sep=',', encoding='EUC-KR', index_col='dates')

"""
df88 = df8[df8.대비2 >0]
df_dm = df88[df88.대비 < 0]
df_dm_am = df_dm[df_dm.거래량대비 <0]
df_dm_ap = df_dm[df_dm.거래량대비 >0]
df_dp = df88[df88.대비 > 0]
df_dp_am = df_dp[df_dp.거래량대비 <0]
df_dp_ap = df_dp[df_dp.거래량대비 >0]
df_d0 = df88[df88.대비 == 0]
df_d0_am = df_d0[df_d0.거래량대비 <0]
df_d0_ap = df_d0[df_d0.거래량대비 >0]
"""

#numbers=[6,5,3,8,4,2,5,4,11]
numbers0=[0,1,2,3]
df8_r = df8[-4:]
거래량_opp0 = df8_r.iloc[1].거래량 / df8_r.iloc[0].거래량
거래량_opp1 = df8_r.iloc[2].거래량 / df8_r.iloc[1].거래량
거래량_opp2 = df8_r.iloc[3].거래량 / df8_r.iloc[2].거래량
diff = df8_r.iloc[3].종가 - df8_r.iloc[0].종가

cnt=0
cnt_d0=0
cnt_d1=0
cnt_d2=0
cnt_d3=0



#df8_t = df8[0:4]



for value in range(len(df8)-4):
    df8_t = df8[value:value+10]
    
    거래량_n_opp0 = df8_t.iloc[1].거래량 / df8_t.iloc[0].거래량
    거래량_n_opp1 = df8_t.iloc[2].거래량 / df8_t.iloc[1].거래량
    거래량_n_opp2 = df8_t.iloc[3].거래량 / df8_t.iloc[2].거래량
    diff_n = df8_t.iloc[3].종가 - df8_t.iloc[0].종가
    
    if 거래량_n_opp0 >= 거래량_opp0 *(1-adjust_amt) and 거래량_n_opp0 <= 거래량_opp0*(1+adjust_amt) :
        if 거래량_n_opp1 >= 거래량_opp1*(1-adjust_amt) and 거래량_n_opp1 <= 거래량_opp1*(1+adjust_amt) :
            if 거래량_n_opp2 >= 거래량_opp2*(1-adjust_amt) and 거래량_n_opp2 <= 거래량_opp2*(1+adjust_amt) :
                if diff >= 0:
                    if diff_n >= diff*(1-adjust_diff) and diff_n <= diff*(1+adjust_diff) :
                        print("lv4 success!!!")
                        print(df8_t)
                        print("4일간 종가의 증감은 ", diff_n)
                        cnt=cnt+1
                        print("다음날 대비 및 대비율은 ", df8_t.iloc[4].대비, "|", df8_t.iloc[4].대비 / df8_t.iloc[4].종가)
                    else: cnt_d0=cnt_d0+1
                else:
                    if diff_n >= diff*(1+adjust_diff) and diff_n <= diff*(1-adjust_diff) :
                        print("lv4 success!!!")
                        print(df8_t)
                        print("4일간 종가의 증감은 ", diff_n)
                        cnt=cnt+1
                        print("다음날 대비 및 대비율은 ", df8_t.iloc[4].대비, "|", df8_t.iloc[4].대비 / df8_t.iloc[4].종가)
                    else: cnt_d0=cnt_d0+1
"""
            else: print("거래량 lv2 failed!")
        else: print("거래량 lv1 failed!")
    else: print("거래량 lv0 failed!")
"""    
print('===================================================================')
print(df8_r)
print("4일간(현재) 종가의 증감은 ", diff)
print("유사 패턴 검출수: ", cnt)
print("cnt_d0 is ", cnt_d0)

"""
    for i in numbers0:
        temp=df8.iloc[value+i]
        temp_index=df8.index[value+i]
#        print(temp_index,"  ",temp.대비, "  ", temp.거래량)
"""
