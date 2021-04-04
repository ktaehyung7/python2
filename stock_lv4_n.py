# -*- coding: utf-8 -*-
"""
Created on Wed May 16 08:20:23 2018

@author: nerguri
"""

import pandas as pd
import numpy as np
import matplotlib as plt

pd.set_option('display.expand_frame_repr', False)

#메리츠 008560, 제넥신 095700, 팜스웰바이오 043090

#df8 = pd.read_csv('C:/Users/nerguri/Desktop/095700_csv.csv', sep=',', encoding='EUC-KR', index_col='일자')
df8 = pd.read_csv('C:/Users/nerguri/Desktop/008560_csv.csv', sep=',', encoding='EUC-KR', index_col='일자')


# adjustment value
adjust_amt = 0.10
adjust_diff = 0.50

# prediction duration
prediction_duration = 8

# list for sorting
a =[0]

# count variables
cnt=0
cnt_d0=0
cnt_up=0
cnt_dn=0
cnt_eq=0
cnt_up_i=0
cnt_dn_i=0
cnt_eq_i=0

# 오름차순 정렬 및 '대비'항목 추
df8 = df8.sort_index(axis=0, ascending=True)

for value in range(len(df8)):
    if value == 0:
        continue
    a_dif = df8.iloc[value].종가 - df8.iloc[value-1].종가
    a.append(a_dif)

df8['대비'] = a

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
    df8_t = df8[value:value+prediction_duration]
    
    거래량_n_opp0 = df8_t.iloc[1].거래량 / df8_t.iloc[0].거래량
    거래량_n_opp1 = df8_t.iloc[2].거래량 / df8_t.iloc[1].거래량
    거래량_n_opp2 = df8_t.iloc[3].거래량 / df8_t.iloc[2].거래량
    diff_n = df8_t.iloc[3].종가 - df8_t.iloc[0].종가
    diff_n_0 = df8_t.iloc[0].대비
    
    if 거래량_n_opp0 >= 거래량_opp0 *(1-adjust_amt) and 거래량_n_opp0 <= 거래량_opp0*(1+adjust_amt) :
        if 거래량_n_opp1 >= 거래량_opp1*(1-adjust_amt) and 거래량_n_opp1 <= 거래량_opp1*(1+adjust_amt) :
            if 거래량_n_opp2 >= 거래량_opp2*(1-adjust_amt) and 거래량_n_opp2 <= 거래량_opp2*(1+adjust_amt) :
                if diff >= 0:
                    if diff_n >= diff*(1-adjust_diff) and diff_n <= diff*(1+adjust_diff) :
                        print("lv4 success!!!")
                        print(df8_t)
                        print("4일간 종가 차이: ", diff_n)
                        print("시작일 대비: ", diff_n_0)
                        cnt=cnt+1
                        print("내일 대비: ", df8_t.iloc[3].대비)
                        # 상승/하락 종목수 count
                        if df8_t.iloc[3].대비 > 0:
                            cnt_up_i=cnt_up_i+1
                        elif df8_t.iloc[3].대비 < 0:
                            cnt_dn_i=cnt_dn_i+1
                        else:
                            cnt_eq_i=cnt_eq_i+1
                    else: cnt_d0=cnt_d0+1
                else:
                    if diff_n >= diff*(1+adjust_diff) and diff_n <= diff*(1-adjust_diff) :
                        print("lv4 success!!!")
                        print(df8_t)
                        print("4일간 종가 차이: ", diff_n)
                        print("시작일 대비: ", diff_n_0)
                        cnt=cnt+1
                        print("내일 대비: ", df8_t.iloc[3].대비)
                        # 상승/하락 종목수 count
                        if df8_t.iloc[3].대비 > 0:
                            cnt_up_i=cnt_up_i+1
                        elif df8_t.iloc[3].대비 < 0:
                            cnt_dn_i=cnt_dn_i+1
                        else:
                            cnt_eq_i=cnt_eq_i+1
                    else: cnt_d0=cnt_d0+1
                if df8_t.iloc[3].대비 > 0:
                    cnt_up=cnt_up+1
                elif df8_t.iloc[3].대비 < 0:
                    cnt_dn=cnt_dn+1
                else:
                    cnt_eq=cnt_eq+1

print('===================================================================')
print(df8_r)
print('===================================================================')
print("4일간(현재) 종가의 증감은 ", diff)
print("종가 흐름 유사 패턴 검출수: ", cnt)
print("종가 흐름 패턴중 상승 검출수: ", cnt_up_i)
print("종가 흐름 패턴중 보합 검출수: ", cnt_eq_i)
print("종가 흐름 패턴중 하락 검출수: ", cnt_dn_i)
print("----------------------------------------------------")
print("거래량 흐름 패턴 검출수(나머지): ", cnt_d0)
print("거래량 흐름 패턴중 상승 검출수: ", cnt_up)
print("거래량 흐름 패턴중 보합 검출수: ", cnt_eq)
print("거래량 흐름 패턴중 하락 검출수: ", cnt_dn)

"""
    for i in numbers0:
        temp=df8.iloc[value+i]
        temp_index=df8.index[value+i]
#        print(temp_index,"  ",temp.대비, "  ", temp.거래량)
"""
