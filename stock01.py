# -*- coding: utf-8 -*-
"""
Created on Wed May 16 08:20:23 2018

@author: nerguri
"""

import pandas as pd
import numpy as np
import matplotlib as plt


#008560
df8 = pd.read_csv('C:/Users/nerguri/Desktop/A008560_1995_m2.csv', sep=',', encoding='EUC-KR', index_col='dates')

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
amount_opp0 = df8.iloc[-3].amount / df8.iloc[-4].amount
amount_opp1 = df8.iloc[-2].amount / df8.iloc[-3].amount
amount_opp2 = df8.iloc[-1].amount / df8.iloc[-2].amount
diff0 = df8.iloc[-4].대비
diff1 = df8.iloc[-3].대비
diff2 = df8.iloc[-2].대비
diff3 = df8.iloc[-1].대비

cnt=0
cnt_d0=0
cnt_d1=0
cnt_d2=0
cnt_d3=0

# adjustment value
adjust_amt = 0.19
adjust_diff = 0.8

#df8_t = df8[0:4]



for value in range(len(df8)-4):
    df8_t = df8[value:value+5]
    
    amount_n_opp0 = df8_t.iloc[1].amount / df8_t.iloc[0].amount
    amount_n_opp1 = df8_t.iloc[2].amount / df8_t.iloc[1].amount
    amount_n_opp2 = df8_t.iloc[3].amount / df8_t.iloc[2].amount
    diff0_n = df8_t.iloc[0].대비
    diff1_n = df8_t.iloc[1].대비
    diff2_n = df8_t.iloc[2].대비
    diff3_n = df8_t.iloc[3].대비

    if amount_n_opp0 >= amount_opp0 *(1-adjust_amt) and amount_n_opp0 <= amount_opp0*(1+adjust_amt) :
        if amount_n_opp1 >= amount_opp1*(1-adjust_amt) and amount_n_opp1 <= amount_opp1*(1+adjust_amt) :
            if amount_n_opp2 >= amount_opp2*(1-adjust_amt) and amount_n_opp2 <= amount_opp2*(1+adjust_amt) :
                if diff0_n >= diff0*(1-adjust_diff) and diff0_n <= diff0*(1+adjust_diff) :
                    if diff1_n >= diff1*(1-adjust_diff) and diff1_n <= diff1*(1+adjust_diff) :
                        if diff2_n >= diff2*(1-adjust_diff) and diff2_n <= diff2*(1+adjust_diff) :
                            if diff3_n >= diff3*(1-adjust_diff) and diff3_n <= diff3*(1+adjust_diff) :
                                print("success!!!")
                                print(df8_t)
                                cnt=cnt+1
                            else: print("diff lv3 failed!");cnt_d3=cnt_d3+1;print(df8_t)
                        else: print("diff lv2 failed!");cnt_d2=cnt_d2+1;print(df8_t)
                    else: print("diff lv1 failed!");cnt_d1=cnt_d1+1;print(df8_t)
                else: print("diff lv0 failed!");cnt_d0=cnt_d0+1
"""
            else: print("amount lv2 failed!")
        else: print("amount lv1 failed!")
    else: print("amount lv0 failed!")
"""    
print('===================================================================')
print(df8_r)

print("total count is ", cnt)
print("cnt_d0 is ", cnt_d0)
print("cnt_d1 is ", cnt_d1)
print("cnt_d2 is ", cnt_d2)
print("cnt_d3 is ", cnt_d3)

"""
    for i in numbers0:
        temp=df8.iloc[value+i]
        temp_index=df8.index[value+i]
#        print(temp_index,"  ",temp.대비, "  ", temp.amount)
"""
