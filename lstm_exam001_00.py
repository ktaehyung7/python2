# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:13:04 2020

@author: nerguri
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense
import keras.backend as K
from keras.callbacks import EarlyStopping
import numpy as np

import matplotlib.pyplot as plt


df = pd.read_csv('c:/Users/nerguri/Desktop/095700.csv', sep=',', encoding='EUC-KR', index_col='일자')

split_date='20170101'
train = df.loc[:split_date,['종가']]
test = df.loc[split_date:, ['종가']]

sc = MinMaxScaler()

train_sc = sc.fit_transform(train)
test_sc = sc.transform(test)

train_sc_df = pd.DataFrame(train_sc, columns=['종가'], index=train.index)
test_sc_df = pd.DataFrame(test_sc, columns=['종가'], index=test.index)

test_sc_df.loc['20200312'] = [0]

for s in range(1,13):
    train_sc_df['shift_{}'.format(s)] = train_sc_df['종가'].shift(s)
    test_sc_df['shift_{}'.format(s)] = test_sc_df['종가'].shift(s)
    
X_train = train_sc_df.dropna().drop('종가', axis=1)
Y_train = train_sc_df.dropna()[['종가']]

X_test = test_sc_df.dropna().drop('종가', axis=1)
Y_test = test_sc_df.dropna()[['종가']]

X_train = X_train.values
Y_train = Y_train.values
X_test = X_test.values
Y_test = Y_test.values

X_train_t = X_train.reshape(X_train.shape[0], 12, 1)
X_test_t = X_test.reshape(X_test.shape[0], 12, 1)

print('최종data')
print('X_train_t.shape: ', X_train_t.shape)
print('X_train_t: ', X_train_t)
print('Y_train: ', Y_train)

#------------------- LSTM 구현 -------------------
K.clear_session()

model = Sequential()
model.add(LSTM(20, input_shape=(12,1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()

early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)

model.fit(X_train_t, Y_train, epochs=100, batch_size=30, verbose=1, callbacks=[early_stop])

score = model.evaluate(X_train_t, Y_train, batch_size=30)

print('mse = ', score)

Y_pred = model.predict(X_test_t, batch_size=32)

plt.figure(figsize=(12,9))
plt.plot(Y_test, label='Y_test')
plt.plot(Y_pred, label='Y_pred')
plt.legend()
plt.show()
