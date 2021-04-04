# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:01:39 2020

@author: nerguri
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

"""MNIST 데이터셋을 로드하여 준비합니다. 샘플 값을 정수에서 부동소수로 변환합니다:"""
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

"""층을 차례대로 쌓아 tf.keras.Sequential 모델을 만듭니다. 훈련에 사용할 
옵티마이저(optimizer)와 손실 함수를 선택합니다:"""
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
              )

"모델 훈련"
model.fit(x_train, y_train, epochs=5)

"모델 평가"
model.evaluate(x_test, y_test, verbose=2)