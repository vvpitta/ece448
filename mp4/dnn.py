# implement data acquisition and algorithm here
import numpy as np
import random as rand
from methods import *

def network(X, weights, biases, y, test):

    Z1, acache1 = affineForward(X, weights[0], biases[0])
    A1, rcache1 = reLUForward(Z1)

    Z2, acache2 = affineForward(A1, weights[1], biases[1])
    A2, rcache2 = reLUForward(Z2)

    Z3, acache3 = affineForward(A2, weights[2], biases[2])
    A3, rcache3 = reLUForward(Z3)

    F, acache4 = affineForward(A3, weights[3], biases[3])

    #do the test thing here

    loss, dF = crossEntropy(F, y)

    dA3, dW4, db4 = affineBackward(dF, acache4)
    dZ3 = reLUBackward(dA3, rcache3)

    dA2, dW3, db3 = affineBackward(dZ3, acache3)
    dZ2 = reLUBackward(dA2, rcache2)

    dA1, dW2, db2 = affineBackward(dZ2, acache2)
    dZ1 = reLUBackward(dA1, rcache1)

    dX, dW1, db1 = affineBackward(dZ1, acache1)

    #update parameters
    dWeights = [dW1, dW2, dW3, dW4]
    dBiases = [db1, db2, db3, db4]
    rate = 0.1

    for idx in range(len(weights)):
        weights[idx] = weights[idx] - (rate * dWeights[idx])
        biases[idx] = biases[idx] - (rate * dBiases[idx])

    return loss
