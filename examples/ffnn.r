#!/usr/bin/env Rscript
# Simple example of a feedforward neural network

relu = function(x) {
	ifelse(x <= 0, 0, x)
}

#activate = tanh
activate = relu

x = c(0, 0, 1) # for example, we're interested in point (0,0), and we add bias term at end

W1 = matrix(c(2.3,  -0.64, 2.0,
			  -3.0, -2, -1,
			  -1.1, 3, 0
			  ), nrow=3)

W2 = c(5, 3, 0, -34)

W3 = -2

# y1 = activate(x %*% W1) # first layer
# y2 = activate(c(y1,1) %*% W2) # second layer

activate(c(activate(x %*% W1),1) %*% W2) # first + second layer
