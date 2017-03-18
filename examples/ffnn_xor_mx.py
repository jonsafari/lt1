#!/usr/bin/env python3
# By Jon Dehdari, 2016-2017
# Minimal example of using MXNet for XOR prediction

import logging
import numpy as np
import mxnet as mx

# Parameters
n_epochs = 300
batch_size = 4

# Configure logging
logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(message)s')


# Build data
xs = np.array([[0,0], [0,1], [1,0], [1,1]])
ys = np.array([0, 1, 1, 0])
data_iter = mx.io.NDArrayIter(xs, label=ys, batch_size=batch_size)

# Build model, using MXNet's Python Symbolic API
net = mx.symbol.Variable('data')

net = mx.symbol.FullyConnected(net, name='fc1', num_hidden=2)
net = mx.symbol.Activation(net, name='relu1', act_type='relu')
net = mx.symbol.FullyConnected(net, name='fc2', num_hidden=4)
net = mx.symbol.SoftmaxOutput(net, name='softmax')

# Use MXNet's Python *Module* API
module = mx.mod.Module(symbol=net, context=mx.cpu(0), data_names=['data'])

module.fit(data_iter, num_epoch=n_epochs, eval_metric='acc',
        #initializer=mx.init.Xavier(factor_type='in'),
        #optimizer_params={'learning_rate':1.0, 'momentum':0.9}
        )

module.save_params('ffnn_xor_mx.params')

print(module.predict(eval_data=data_iter).asnumpy())
