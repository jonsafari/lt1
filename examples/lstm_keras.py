#!/usr/bin/env python3
# By Jon Dehdari, 2017

""" Simple example of Keras learning a sequence using an LSTM. """

import numpy as np
import keras as kr
from keras.layers import Dense, Dropout, recurrent

batch_size = 8
n_epochs = 1000
np.random.seed(3)

# Build data
# Fibonacci sequence
X = np.array([[1,1,2], [1,2,3], [2,3,5], [3,5,8], [5,8,13], [8,13,21], [13,21,34], [21,34,55]])
y = np.array([3,5,8,13,21,34,55,89])
vocab = set(list(X.flatten()) + list(y.flatten()))
vocab_size = len(vocab)

# Reshape so that each value is its own array.
X = np.reshape(X, (len(X),-1,1))
y = kr.utils.np_utils.to_categorical(y)

# Build model, using Keras' Sequential model
model = kr.models.Sequential()
model.add(recurrent.GRU(12, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.1))
model.add(Dense(y.shape[1], activation='softmax'))

# Compile model
model.compile(loss='categorical_crossentropy', optimizer=kr.optimizers.Adam(lr=0.05), metrics=['accuracy'])

# Fit model to our data
model.fit(x = X, y = y, nb_epoch = n_epochs, batch_size = batch_size)

example_x = X[5]
example_out = model.predict(np.reshape(example_x, (1, len(example_x), 1)))
example_argmax = np.argmax(example_out.flatten())
example_correct = np.argmax(y[5])
print("\nOverall training [loss, accuracy] is", model.evaluate(X, y))
print("\nExample input: %s\n Guess: %s\n Correct: %s" %
        (example_x.flatten(), example_argmax, example_correct))

model.save_weights("lstm_keras.weights", overwrite=True)
