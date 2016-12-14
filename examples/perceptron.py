#!/usr/bin/env python3
# By Jon Dehdari, 2016

"""
This is an implementation of a single-layer perceptron.
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
test_size = int(num_samples / 100 * test_percentage)	# This line was changed, so that the test size actually reflects the specified percentage.
train_size = num_samples - test_size


class Perceptron(list):
    """ This class implements a single-layer perceptron. The following lines are
        an example for how to use the perceptron and plot the results on a graph.

    >>> fig = plt.figure()
    >>> subplot = fig.add_subplot(1,1,1, xlim=(-5,5), ylim=(-5,5))
    >>> train_set = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1)]
    >>> test_set  = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1)]
    >>> p = Perceptron(2)
    >>> p.train(train_set, test_set, status=10, subplot=subplot, fig=fig)
    """

    def __init__(self, num_inputs, learning_rate=learning_rate):
        self.params = np.random.normal(size=num_inputs)		# A list that contains num_inputs random numbers
        self.bias   = np.random.normal()			# Randomly chosed bias
        self.learning_rate = learning_rate

    def __repr__(self):
        """ Returns:
                A String representation of the perceptron.
                The preceptron can be represented by the parameters plus the bias.
        """
        return str(np.concatenate((self.params, [self.bias])))


    def error(self, guess, correct):
        return correct - guess


    def activate(self, val, fun='step'):
        """ The non-linear activation function of the perceptron.

            Args:
                val: The weighted sum of the inputs for which we want to compute the activation.
                fun: The activation function that should be used. 'step' function is the default.

            Returns:
                The activation for a given value.
        """
        if fun == 'step':
            if val >= 0:
                return 1
            else:
                return 0

        elif fun == 'tanh':
            return np.tanh(val)


    def predict(self, x):
        """ Predicts the activation of the perceptron by feeding the scalar product
            of the input vector and the weights (parameters) of the perceptron
            into the activation function.

            Args:
                x: Input vector

            Returns:
                The activation of the perceptron given an input vector
        """
        #if 0 > np.tanh(np.dot(x, self.params) + self.bias):
        return self.activate(np.dot(x, self.params) + self.bias)  


    def predict_set(self, test_set):
        errors = 0

        # Count the number of times where the perceptron doesn't
        # predict the correct output for a given test set.
        for x, y in test_set:
            out = self.predict(x)
            if out != y:
                errors +=1  
        return 1 - errors / len(test_set)   # Returns the percentage of correctly predicted test samples


    def decision_boundary(self):
        """ Returns two points, along which the decision boundary for a binary classifier lies. """
        return ((0, -self.bias / self.params[1]), (-self.bias / self.params[0], 0)) # This only works if the perceptron is initialized with two input nodes?


    def train(self, train_set, dev_set, status=100, epochs=10, subplot=None, fig=None):
        """ Train the perceptron on a given training set by updating the parameters.

            Args:
                train_set: A list of the training samples to be trained on.
                dev_set: A list of the development samples for evaluation.
                status: Number of iterations after which a status update is printed to the console. Default is 100.
                epochs: Number of times to iterate over the whole training set. Default is 10.
                subplot: Plot that shows the performance of the perceptron.
                fig: Figure that contains the plot.
        """
        print("Starting dev set accuracy: %g; Line at %s; Params=%s" % (self.predict_set(dev_set), str(self.decision_boundary()), str(self)), file=sys.stderr)
        subplot.plot([0, -self.bias/self.params[1]], [-self.bias/self.params[0], 0], '-', color='lightgreen', linewidth=1)
        fig.canvas.draw()

        iterations = 0
        for epoch in range(epochs):
            np.random.shuffle(train_set)  # Iterate over the training set in a different order during each epoch.
            for x, y in train_set:
                iterations += 1
                out = self.predict(x)
                error = self.error(out, y)
                if error != 0:
                    #print("out=", out, "; y=", y, "; error=", error, file=sys.stderr)
                    self.bias += self.learning_rate * error  # Update the bias by the learning rate. Will be increased for a positive error and decreased for a negative error.
                    for i in range(len(x)):
                        # Update the parameters. Parameters corresponding to larger input values will be changed more drastically
                        # as they have a higher influence on the output/error.
                        self.params[i] += self.learning_rate * error * x[i]
                if iterations % status == 0:
                    print("Dev set accuracy: %g; Line at %s; Params=%s" % (self.predict_set(dev_set), str(self.decision_boundary()), str(self)), file=sys.stderr)
                    subplot.plot([0, -self.bias/self.params[1]], [-self.bias/self.params[0], 0], '-', color='lightgreen', linewidth=1)
                    fig.canvas.draw()
            self.learning_rate *= 0.9  # Decrease the learning rate after each epoch, so that the parameters change less during later stages of the training when they should be closer to their desired values.
        subplot.plot([0, -self.bias/self.params[1]], [-self.bias/self.params[0], 0], 'g-x', linewidth=5)
        fig.canvas.draw()


def main():
    import doctest
    doctest.testmod()  # Test the provided example code in the docstring

    # Generate normally distributed data points for two different 'classes'
    x_blue = np.random.normal(loc=0, size=num_samples)
    y_blue = np.random.normal(loc=0, scale=0.5, size=num_samples)
    x_red  = np.random.normal(loc=2, size=num_samples)
    y_red  = np.random.normal(loc=2, scale=0.5, size=num_samples)
    
    data =  list(zip(zip(x_blue, y_blue), [labels[0]] * num_samples))   # Blue data points are classified as 0
    data += zip(zip(x_red,  y_red),  [labels[1]] * num_samples)         # Red data points are classified as 1
    np.random.shuffle(data)  # Randomly reorder the data points, so the perceptron will not be presented all the data points from one class first during training
    
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
