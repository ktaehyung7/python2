### 데이터 불러오기
import os
# 현재 경로
path=os.getcwd()
# 경로 변경
#path = os.path.abspath( "stock_predict/data") # 본인 환경에 맞게 변경할 것
os.chdir(path)
import warnings
warnings.filterwarnings('ignore')

import datetime
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np

tf.random.set_seed(314)

### pandas의 dataframe 형태로 저장하기  
stock_file_name = 'AAPL.csv' 
encoding = 'euc-kr' 
names = ['Date','Open','High','Low','Close','AdjClose','Volume']
raw_dataframe = pd.read_csv(stock_file_name, names=names, encoding=encoding) 
raw_dataframe.info() 

raw_dataframe = raw_dataframe.dropna(axis=0)

df_price = pd.DataFrame(raw_dataframe)
df_price.columns
df_price.describe()

### sklearn 패키지에 있는 MinMaxScaler를 활용하여 전체 학습 데이터를 정규화하기
    # MinMaxScaler를 해주면 전체 데이터는 0(min값),1(max값) 사이의 값을 갖게 됨

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scale_cols = ['Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume']
df_scaled = scaler.fit_transform(df_price[scale_cols])
df_scaled = pd.DataFrame(df_scaled)
df_scaled.columns = scale_cols

print(df_scaled)

### 학습데이터셋과 테스트 데이터셋 생성하기

#TEST_SIZE=30 -> 학습은 과거부터 30일 이전의 데이터를 학습하게 되고, TEST를 위해서 이후 30일의 데이터로
# 모델이 주가를 예측하도록 한 다음, 실제 데이터와 오차가 얼마나 있는지 확인해보기 
TEST_SIZE = 30
train = df_scaled[:-TEST_SIZE]
test = df_scaled[-TEST_SIZE:]


# dataset을 만들어주는 함수. 정해진 window_size에 기반하여 5일 기간의 데이터셋을 묶어주는 역할을 하는 함수
# 순차적으로 5일 동안의 데이터 셋을 묶고, 이에 맞는 label(예측 데이터)와 함께 return해줌
# window_size는 내가 얼마 동안(기간)의 주가 데이터에 기반하여 다음날 종가를 예측할 것인가를 정하는 parameter
# 과거 5일을 기반으로 내일 데이터를 예측한다고 가정했을 때, window_size=5

def make_dataset(data, label, window_size = 5):
    feature_list = []
    label_list = []
    for i in range(len(data) - window_size):
        feature_list.append(np.array(data.iloc[i:i+window_size]))
        label_list.append(np.array(label.iloc[i+window_size]))
    return np.array(feature_list), np.array(label_list)

# feature와 label 정의하기
feature_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
label_cols = ['AdjClose']

train_feature = train[feature_cols]
train_label = train[label_cols]

# train dataset
train_feature, train_label = make_dataset(train_feature, train_label, 6)

# train, validation set 생성
from sklearn.model_selection import train_test_split
x_train, x_valid, y_train, y_valid = train_test_split(train_feature, train_label, test_size = 0.2)

x_train.shape, x_valid.shape

# test dataset
test_feature = test[feature_cols]
test_label = test[label_cols]

# test dataset (실제 예측해볼 데이터))
test_feature, test_label = make_dataset(test_feature, test_label, 6)
test_feature.shape, test_label.shape

# Keras를 활용한 LSTM 모델 생성
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM

model = Sequential()
model.add(LSTM(16,
               input_shape = (train_feature.shape[1], train_feature.shape[2]),
               activation='relu',
               return_sequences=False)
          )
model.add(Dense(1))

# 모델 학습하기
model.compile(loss='mean_squared_error', optimizer='adam')
early_stop = EarlyStopping(monitor='val_loss', patience=5)
filename = 'tmp_checkpoint.h5'
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')

history = model.fit(x_train, y_train,
                    epochs = 200,
                    batch_size = 16,
                    validation_data = (x_valid, y_valid),
                    callbacks = [early_stop, checkpoint])

## 학습한 모델로 미래 주가 예측해보기
# weight 로딩
model.load_weights(filename)
# 예측
pred = model.predict(test_feature)

# 그래프 확인
plt.figure(figsize=(12,9))
plt.plot(test_label, label='actual')
plt.plot(pred, label='prediction')
plt.legend()
plt.show()

