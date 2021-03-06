# -*- coding: utf-8 -*-
"""Keras를 이용한 간단한 이미지 분류.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p3zQoO7naps7wuvwcXSeKVgoV-pmV9QS
"""

import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터 탐색
mnist_data = tf.keras.datasets.mnist # mnist라는 데이터를 불러오는거
(train_images, train_labels), (test_images, test_labels) = mnist_data.load_data()

# 데이터가 제대로 들어갔는지 확인
train_images.shape
train_labels.shape

# matplotlib를 이용해서 좀 더 직관적으로 확인
plt.figure(figsize=(10,10))
for i in range(25):
  plt.subplot(5, 5, i+1)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(train_images[i], cmap=plt.cm.binary)
  plt.xlabel(train_labels[i])
plt.show()

# 훈련하기에 적합하도록 전처리 과정
train_images = train_images.astype('float32')
train_images = train_images / 255

test_images = test_images.astype('float32')
test_images = test_images / 255

# 2.모델 구성
model = keras.Sequential([
                          keras.layers.Flatten(input_shape=(28, 28)),
                          keras.layers.Dense(128, activation=tf.nn.relu),
                          keras.layers.Dropout(0,1),
                          keras.layers.Dense(10, activation=tf.nn.softmax)
])

# 적절한 최적화 옵션을 넣고 컴파일
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 3. 모델 훈련
model.fit(train_images, train_labels, epochs=10)

# 4. 평가 // loss는 낮아야하고, acc는 높아야 함.
loss, acc = model.evaluate(test_images, test_labes)
print('Loss: {}, Acc: {}'.format(loss, acc))