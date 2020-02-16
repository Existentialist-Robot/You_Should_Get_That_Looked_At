# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:35:34 2020

@author: mengh
"""

import tensorflow as tf
import os, sys, math,json, shutil
import IPython.display as display
import numpy as np
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as plt
from tensorflow.keras.utils import to_categorical
import cv2

from sklearn.model_selection import train_test_split

dx_map = {
    'nv': 0,
    'mel': 1,
    'bkl': 2,
    'df': 3,
    'akiec': 4,
    'bcc': 5,
    'vasc': 6
}

dx_type_map = {
    'follow_up': 0,
    'histo': 1,
    'consensus': 2
}

sex_map = {
    'male': 0,
    'female': 1
}

localization_map = {
    'lower extremity': 0,
    'trunk': 1,
    'chest': 2,
    'abdomen': 3,
    'foot': 4,
    'upper extremity': 5
}

img_dir = 'C:\\Users\\mengh\\Yeet_Brain\\HAM10000_images_part_1'
img_dir2 = 'C:\\Users\\mengh\\Yeet_Brain\\HAM10000_images_part_2'

df = pd.read_csv('C:\\Users\\mengh\\Yeet_Brain\\HAM10000_metadata.csv')

label_df = df[['image_id','dx']]

training_data = []

limit = 3000

def create_training_data_ints():
  counter = 0
  for index, row in label_df.iterrows():

    if counter >= limit: break

    img_name = row['image_id']
    img_path = os.path.join(img_dir,img_name+'.jpg')
    img_array = cv2.imread(img_path)

    if img_array is None: # check second folder
      img_path = os.path.join(img_dir2,img_name+'.jpg')
      img_array = cv2.imread(img_path)
      class_text = row['dx']
      training_data.append([img_array,dx_map[row['dx']]])
      pass

    class_text = row['dx']
    #print(class_text, type(class_text))
    training_data.append([img_array,dx_map[row['dx']]])
    print('finished:', counter)
    print('file:', img_name)
    print((index+1)/limit*100,'% done')

    counter += 1

create_training_data_ints()

df.dtypes

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, 450, 600, 3)
y = np.array(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model2 = tf.keras.models.Sequential([
     tf.keras.layers.Conv2D(16, (8, 8), activation = 'relu', padding = 'same', input_shape = [450,600,3]),
     tf.keras.layers.MaxPooling2D(4,4),
     tf.keras.layers.Conv2D(32, (5, 5),activation = 'relu', padding = 'same'),
     tf.keras.layers.Conv2D(64, (5, 5),activation = 'relu', padding = 'same'),
     tf.keras.layers.MaxPooling2D(4,4),
     tf.keras.layers.Flatten(),
     tf.keras.layers.Dense(128,activation = 'relu'),
     tf.keras.layers.Dropout(0.5),
     tf.keras.layers.Dense(7,activation = 'softmax')
])

model2.compile(
  optimizer='adam',
  loss='sparse_categorical_crossentropy',
  metrics=['accuracy']) # % of correct answers

# train the model
history = model2.fit(X, y, batch_size=32, epochs=10, validation_split=0.2)

dx_position = {
    0:'bkl',
    1:'mel',
    2:'df',
    3:'nv',
    4:'vasc',
    5:'bcc'
}

test_im = cv2.imread('/content/drive/My Drive/CalgaryHacks2020/dataverse_files/HAM10000_images_part_1/ISIC_0029538.jpg')
test_images = []
test_images.append(test_im)
test_images = np.asarray(test_images)
result = model2.predict(test_images)
print(result[0])
max_result = max(result[0])


for i in range(len(result[0])):
  if max_result == result[0][i]:
    print('The model predicted with probablity of', max_result*100, 'that the image is symptomatic of', dx_position[i])
