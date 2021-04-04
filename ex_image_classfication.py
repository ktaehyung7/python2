# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:12:15 2020

@author: nerguri
"""

from __future__ import absolute_import, division, print_function, unicode_literals

"#tensorflow와 tf.keras를 임포트"
import tensorflow as tf
from tensorflow import keras

"#헬퍼(helper) 라이브라리를 임포트"
import numpy as np
import matplotlib.pyplot as plt

#print(tf.__version__)

"""10개의 범주(category)와 70,000개의 흑백 이미지로 구성된 패션 MNIST 데이터셋을 
사용하겠습니다. 이미지는 해상도(28x28 픽셀)가 낮고 다음처럼 개별 옷 품목을 나타냅니다:
패션 MNIST는 컴퓨터 비전 분야의 "Hello, World" 프로그램격인 고전 MNIST 데이터셋을 
대신해서 자주 사용됩니다. MNIST 데이터셋은 손글씨 숫자(0, 1, 2 등)의 이미지로 이루어져 
있습니다. 여기서 사용하려는 옷 이미지와 동일한 포맷입니다.
패션 MNIST는 일반적인 MNIST 보다 조금 더 어려운 문제이고 다양한 예제를 만들기 위해 
선택했습니다. 두 데이터셋은 비교적 작기 때문에 알고리즘의 작동 여부를 확인하기 위해 
사용되곤 합니다. 코드를 테스트하고 디버깅하는 용도로 좋습니다.
네트워크를 훈련하는데 60,000개의 이미지를 사용합니다. 그다음 네트워크가 얼마나 정확하게
 이미지를 분류하는지 10,000개의 이미지로 평가하겠습니다. 패션 MNIST 데이터셋은 텐서플로
 에서 바로 임포트하여 적재할 수 있습니다:
"""
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat'
               , 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255
test_images = test_images / 255

# 층 구성
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 학습
model.fit(train_images, train_labels, epochs=5)

# 정확도 평가
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\n테스트 정확도: ', test_acc)

def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    
    plt.imshow(img, cmap=plt.cm.binary)
    
    predicted_label = np.argmax(predictions_arrary)
    if predicted_label == true_label:
        color = 'blue'
    else :
        color = 'red'
        
    plt.xlabel("{} {:2.0f ({})".format(class_names[predicted_label],
                                       100*np.max(predictions_array),
                                       class_names[true_label]),
               color=color)
    
def plot_value_array(i, predictions_arrary, true_label):
    predictions_arrary, true_label = predictions_arrary[i], true_label[i]
    
            

plt.figure(figsize=(10,10))
for i in range(25) :
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
  
plt.show()

