#Brandberg classifier
from __future__ import division, print_function, absolute_import
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from tflearn.data_utils import resize_image

import tensorflow as tf
import tflearn
from tflearn.data_utils import shuffle, to_categorical
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression

tf.reset_default_graph()

#network
network = input_data(shape=[None, 180, 160, 4])
network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 2)
network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 2)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.001)

model = tflearn.DNN(network, tensorboard_verbose=2)
model.load("./models/master/brandberg.tflearn")

#classifier
try:
	imagePath = Path("input.png")
	img = Image.open(imagePath)
	img.load()
	img = resize_image(img, 160, 180)
	data = np.asarray(img, dtype="float32")
	data /= 255
	data = np.reshape(data, (1, 180, 160, 4))
	result = model.predict(data)

	#Ergebnis der Classification in Kreisdiagramm speichern
	import matplotlib.pyplot as plt

	labels = ['Male', 'Female']
	sizes = [str(result[0][0]),str(result[0][1])]
	colors = ['#ff9999','#66b3ff']
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
	ax1.axis('equal')
	plt.tight_layout()

	#speichert Grafik auf in htdocs-Ordner auf Computer (sofern Pfad stimmt)
	plt.savefig('/xampp/htdocs/result.png')

	#gibt Klassifikationsergebnis in alert auf Seite aus
	#print('Male   (' + str(result[0][0]) + ')   Female (' + str(result[0][1]) + ')')

except FileNotFoundError:
	print('File not found.')