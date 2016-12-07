#!/usr/bin/env python3
# By Jon Dehdari, 2016

""" ...
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

labels = [0, 1]
#num_samples = 30
num_samples = 200
np.random.seed(seed=3)
learning_rate = 1.0
test_percentage = 10
test_size = num_samples // test_percentage
train_size = num_samples - test_size


class Perceptron(list):
    """ ...

    >>> fig = plt.figure()
    >>> subplot = fig.add_subplot(1,1,1, xlim=(-5,5), ylim=(-5,5))
    >>> train_set = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1)]
    >>> test_set  = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1)]
    >>> p = Perceptron(2)
    >>> p.train(train_set, test_set, status=10, subplot=subplot, fig=fig)
    """

    def __init__(self, num_inputs, learning_rate=learning_rate):
        self.params = np.random.normal(size=num_inputs)
        self.bias   = np.random.normal()
        self.learning_rate = learning_rate

    def __repr__(self):
        return str(np.concatenate((self.params, [self.bias])))


    def error(self, guess, correct):
        return correct - guess


    def activate(self, val, fun='step'):
        if fun == 'step':
            if val >= 0:
                return 1
            else:
                return 0

        elif fun == 'tanh':
            return np.tanh(val)


    def predict(self, x):
        #if 0 > np.tanh(np.dot(x, self.params) + self.bias):
        return self.activate(np.dot(x, self.params) + self.bias)  # ...


    def predict_set(self, test_set):
        errors = 0
        for x, y in test_set:
            out = self.predict(x)
            if out != y:
                errors +=1  
        return 1 - errors / len(test_set)


    def decision_boundary(self):
        """ Returns two points, along which the decision boundary for a binary classifier lies. """
        return ((0, -self.bias / self.params[1]), (-self.bias / self.params[0], 0))


    def train(self, train_set, dev_set, status=100, epochs=10, subplot=None, fig=None):
        """ ... """
        print("Starting dev set accuracy: %g; Line at %s; Params=%s" % (self.predict_set(dev_set), str(self.decision_boundary()), str(self)), file=sys.stderr)
        subplot.plot([0, -self.bias/self.params[1]], [-self.bias/self.params[0], 0], '-', color='lightgreen', linewidth=1)
        fig.canvas.draw()

        iterations = 0
        for epoch in range(epochs):
            np.random.shuffle(train_set)  # ...
            for x, y in train_set:
                iterations += 1
                out = self.predict(x)
                error = self.error(out, y)
                if error != 0:
                    #print("out=", out, "; y=", y, "; error=", error, file=sys.stderr)
                    self.bias += self.learning_rate * error # ...
                    for i in range(len(x)):
                        self.params[i] += self.learning_rate * error * x[i]  # ...
                if iterations % status == 0:
                    print("Dev set accuracy: %g; Line at %s; Params=%s" % (self.predict_set(dev_set), str(self.decision_boundary()), str(self)), file=sys.stderr)
                    subplot.plot([0, -self.bias/self.params[1]], [-self.bias/self.params[0], 0], '-', color='lightgreen', linewidth=1)
                    fig.canvas.draw()
            self.learning_rate *= 0.9  # ...
        subplot.plot([0, -self.bias/self.params[1]], [-self.bias/self.params[0], 0], 'g-x', linewidth=5)
        fig.canvas.draw()


def main():
    import doctest
    doctest.testmod()  # ...

    # ...
    x_blue = np.random.normal(loc=0, size=num_samples)
    y_blue = np.random.normal(loc=0, scale=0.5, size=num_samples)
    x_red  = np.random.normal(loc=2, size=num_samples)
    y_red  = np.random.normal(loc=2, scale=0.5, size=num_samples)
    
    data =  list(zip(zip(x_blue, y_blue), [labels[0]] * num_samples))
    data += zip(zip(x_red,  y_red),  [labels[1]] * num_samples)
    np.random.shuffle(data)  # ...
    
    train_set = data[:train_size]
    test_set  = data[train_size:]
    
    # Matplotlib craziness to be able to update a plot
    plt.ion()
    fig = plt.figure()
    subplot = fig.add_subplot(1,1,1, xlim=(-5,5), ylim=(-5,5))
    subplot.grid()
    subplot.plot(x_blue, y_blue, linestyle='None', marker='o', color='blue')
    subplot.plot(x_red,  y_red,  linestyle='None', marker='o', color='red')

    p = Perceptron(2)
    p.train(train_set, test_set, subplot=subplot, fig=fig)


if __name__ == '__main__':
    main()
