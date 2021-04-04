# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:30:02 2020

@author: nerguri
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense
import keras.backend as K
from keras.callbacks import EarlyStopping


df = pd.read_csv('C:/Users/nerguri/Desktop/095700.csv', sep=',', encoding='EUC-KR', index_col='일자')

#df['종가'].plot()

split_date = '20170101'

train = df.loc[:split_date, ['종가']]
test = df.loc[split_date:, ['종가']]


#ax = train.plot()
#test.plot(ax=ax)
#plt.legend(['train', 'test'])

sc = MinMaxScaler()

train_sc = sc.fit_transform(train)
test_sc = sc.transform(test)


train_sc_df = pd.DataFrame(train_sc, columns=['종가'], index=train.index)
test_sc_df = pd.DataFrame(test_sc, columns=['종가'], index=test.index)

for s in range(1,13):
    train_sc_df['shift_{}'.format(s)] = train_sc_df['종가'].shift(s)
    test_sc_df['shift_{}'.format(s)] = test_sc_df['종가'].shift(s)
    

X_train = train_sc_df.dropna().drop('종가', axis=1)
Y_train = train_sc_df.dropna()[['종가']]

X_test = test_sc_df.dropna().drop('종가', axis=1)
Y_test = test_sc_df.dropna()[['종가']]

X_train = X_train.values
X_test = X_test.values
Y_train = Y_train.values
Y_test = Y_test.values

print(X_train.shape)
print(Y_train.shape)


X_train_t = X_train.reshape(X_train.shape[0], 12, 1)
X_test_t = X_test.reshape(X_test.shape[0], 12, 1)

print('최종 DATA')
print(X_train_t.shape)
print(X_train_t)
print(Y_train)

#------------ LSTM -------------------
K.clear_session()

model = Sequential()
model.add(LSTM(20, input_shape=(12,1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()

early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)

model.fit(X_train_t, Y_train, epochs=100, batch_size=30, verbose=1
          , callbacks=[early_stop])

score = model.evaluate(X_test_t, Y_test, batch_size=30)
print("mse = ", score)

y_pred = model.predict(X_test_t, batch_size=32)
#plt.scatter(Y_test, y_pred)
#plt.xlabel("Price Index: $Y_i$")
#plt.ylabel("Predicted price Index: $\hat{Y}_i$")
#plt.title("Prices vs Predicted price Index: $Y_i$ vs $\hat{Y}_i$")

plt.figure(figsize=(12,9))
plt.plot(Y_test, label='test')
plt.plot(y_pred, label='prediction')
plt.legend()
plt.show()
