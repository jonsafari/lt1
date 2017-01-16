#!/usr/bin/env python3
# By Jon Dehdari, 2017

""" Simple example of Keras learning the XOR function. """

#import logging
import numpy as np
import keras as kr
from keras.layers import Dense

batch_size = 4
n_epochs = 1000
init = 'glorot_normal'

# Build data
xs = np.array([[0,0], [0,1], [1,0], [1,1]])
ys = np.array([0, 1, 1, 0])
#np.random.seed(3)

# Configure logging
#logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s %(message)s')

# Build model, using Keras' Sequential model
model = kr.models.Sequential()
model.add(Dense(init=init, activation='sigmoid', input_dim=2, output_dim=4))
model.add(Dense(init=init, activation='sigmoid', output_dim=1))

# Compile model
model.compile(loss='binary_crossentropy', optimizer=kr.optimizers.Adam(lr=0.3), metrics=['accuracy'])

# Fit model to our data
model.fit(x = xs, y = ys, nb_epoch = n_epochs, batch_size = batch_size)

print("Predictions on training data are:", model.predict_classes(xs))
print("which gives a [loss, accuracy] of", model.evaluate(xs, ys))
