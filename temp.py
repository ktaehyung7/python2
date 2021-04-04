# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib as plt

s = pd.Series([1,3,5,np.nan,6,8])

dates = pd.date_range('20180101', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A' :1.,
                   'B' : pd.Timestamp('20180102'),
                   'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D' : np.array([3] * 4, dtype='int32'),
                   'E' : pd.Categorical(["test", "train","test","train"]),
                   'F' : 'foo'})

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20180102', periods=6))
df['F']=s1

df1 = df.reindex(index=dates[0:4], columns=list(df.columns)+['E'])

s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)

s = pd.Series(np.random.randint(0,7,size=10))

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

df = pd.DataFrame(np.random.randn(10,4))

pieces = [df[:3], df[3:7], df[7:]]

left = pd.DataFrame({'key':['foo', 'foo'], 'lval':[1,2]})

right = pd.DataFrame({'key':['foo','foo'], 'rval':[4,5]})

left = pd.DataFrame({'key':['foo', 'bar'], 'lval':[1,2]})

right = pd.DataFrame({'key':['foo','bar'], 'rval':[4,5]})

#Append
df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])  

#grouping
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two','two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

#reshaping
tuples = list(zip(*[['bar','bar','baz','baz','foo','foo','qux', 'qux'],
                     ['one','two','one','two','one','two','one','two']]))


index = pd.MultiIndex.from_tuples(tuples,names=['first','second'])
df = pd.DataFrame(np.random.randn(8,2), index=index,columns=['A','B'])
df2 = df[:4]


#008560
df8 = pd.read_csv('C:/Users/nerguri/Desktop/A008560_1995_m2.csv', sep=',', encoding='EUC-KR', index_col='dates')
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




# for loop


numbers=[6,5,3,8,4,2,5,4,11]

sum=0
for val in range(len(numbers)):
    sum = sum+val
else:
    print("finish")
    
print("sum =", sum)


# file

f = open('C:/Users/nerguri/Documents/aa.txt', 'w')
f.write('This is a test\n')

f.close()


#in/out
a = input()
print(a)


#Class
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#Class2
class FourCal:
    def setdata(self, first, second):
        self.first = first;
        self.second = second;
        

a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,7)

print(a.first)
print(a.second)
print(b.first)
print(b.second)
