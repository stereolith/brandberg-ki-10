
#teile aus https://github.com/tflearn/tflearn/blob/master/examples/images/convnet_cifar10.py

from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.data_utils import shuffle, to_categorical
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_utils import image_preloader
import tensorflow as tf

import sys
from pathlib import Path

import numpy as np
from PIL import Image
from tflearn.data_utils import resize_image

tf.reset_default_graph()

#Load Datasets
X, Y = image_preloader('C:\\Users\\lukas\\Documents\\Uni\\KI\\kat\\ROOT', image_shape=(200, 250), mode='folder' , categorical_labels=True, normalize=True)
testX, testY = image_preloader('C:\\Users\\lukas\\Documents\\Uni\\KI\\kat\\TEST', image_shape=(200, 250), mode='folder', categorical_labels=True, normalize=True)

#Convolutional Neural Network
network = input_data(shape=[None, 250, 200, 4])
network = conv_2d(network, 32, 3, activation='relu')
network = max_pool_2d(network, 2)
network = conv_2d(network, 64, 3, activation='relu')
network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 2)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.001)

#training
model = tflearn.DNN(network, tensorboard_verbose=2)
model.fit(X, Y, n_epoch=12, shuffle=True, validation_set=(testX, testY), show_metric=True, batch_size=96, run_id='brandberg')


#classifier
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   END = '\033[0m'

while True:
	cin = input('image path: ')
	imagePath = Path(cin)

	img = Image.open(imagePath)
	img.load()
	img = resize_image(img, 200, 250)

	data = np.asarray(img, dtype="float32")
	data /= 255
	data = np.reshape(data, (1, 250, 200, 4))
	result = model.predict(data)
	print(color.BLUE + 'Result:' + color.END)
	if result[0][0] > .5:
		if result[0][0] > .9:
			print(color.GREEN + 'Male   (' + str(result[0][0]) + ')' + color.END)
			print(color.RED + 'Female (' + str(result[0][1]) + ')' + color.END)
		else:
			print(color.CYAN + 'Male   (' + str(result[0][0]) + ')' + color.END)
			print(color.BLUE + 'Female (' + str(result[0][1]) + ')' + color.END)
	elif result[0][0] < .1:
		print(color.RED + 'Male   (' + str(result[0][0]) + ')' + color.END)
		print(color.GREEN + 'Female (' + str(result[0][1]) + ')' + color.END)
	else:
		print(color.BLUE + 'Male   (' + str(result[0][0]) + ')' + color.END)
		print(color.CYAN + 'Female (' + str(result[0][1]) + ')' + color.END)