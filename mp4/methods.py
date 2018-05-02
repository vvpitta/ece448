# This file will be for all the functions for dnn
import numpy as np
from scipy.misc import logsumexp
import random as rand
import math
from cache import *

'''
    Method: extract
    Inputs: filename
    Outputs: data
    Description: This file takes the raw text and creates data that can be manipulated
'''
def extract(filename):

    file = open(filename, 'r')

    data = np.zeros((10000, 6))
    i = 0

    for line in file:
        line = line.split()
        for idx in range(len(line)):
            line[idx] = float(line[idx])
        data[i] = line
        i += 1

    file.close()

    return data

'''
    Method: weightsBiases
    Inputs: Dimensions for hidden layers
    Outputs: The initial weight and bias arrays
    Description: This method initializes weights and biases that will be used in the neural
                    net algorithm
'''
def weightsBiases(d, d1, d2, d3, d4, parameter):

    w_1 = np.zeros((d, d1))
    w_2 = np.zeros((d1, d2))
    w_3 = np.zeros((d2, d3))
    w_4 = np.zeros((d3, d4))

    b_1 = np.zeros(d1)
    b_2 = np.zeros(d2)
    b_3 = np.zeros(d3)
    b_4 = np.zeros(d4)

    for mat in [w_1, w_2, w_3, w_4]:
        for x in range(mat.shape[0]):
            for y in range(mat.shape[1]):
                mat[x][y] = round(rand.uniform(0, 1), 3) * parameter

    return [w_1, w_2, w_3, w_4], [b_1, b_2, b_3, b_4]

'''
    Method: affineForward
    Inputs: Arrays for modification
    Outputs: Return output for affine forward
    Description: The first function for forward propagation
'''
def affineForward(A, W, b):

    Z = np.dot(A, W) + b
    cache = AffineCache(A, W, b)

    return Z, cache

'''
    Method: reLUForward
    Inputs: Arrays for modification
    Outputs: Return output for reLUForward forward
    Description: The second function for forward propagation
'''
def reLUForward(Z):

    A = Z

    Zchange = np.where(A < 0)
    A[A < 0] = 0

    cache = ReLUCache(Z, Zchange)

    return A, cache

'''
    Method: affineBackward
    Inputs: Arrays for modification
    Outputs: Return output for affine backward
    Description: The first function for backward propagation
'''
def affineBackward(dZ, cache):

    A, W, b = cache.getAll()

    dA = np.zeros(A.shape)
    dW = np.zeros(W.shape)
    db = np.zeros(b.shape)

    dA = np.dot(dZ, np.transpose(W))

    dW = np.dot(np.transpose(A), dZ)

    db = np.sum(dZ, axis=0)

    return dA, dW, db

'''
    Method: reLUBackward
    Inputs: Arrays for modification
    Outputs: Return output for reLU backward
    Description: The first function for backward propagation
'''
def reLUBackward(dA, cache):

    Z, Zchange = cache.getAll()

    dZ = dA

    x = Zchange[0]
    y = Zchange[1]

    for idx in range(len(x)):
        dZ[x[idx]][y[idx]] = 0

    return dZ

'''
    Method: crossEntropy
    Inputs: Arrays for modification
    Outputs: The loss of the net
    Description: This method returns the loss of the function
'''
def crossEntropy(F, y):

    n = F.shape[0]
    dF = np.zeros(F.shape)

    total = 0
    for i in range(F.shape[0]):
        sum1 = 0
        for k in range(3):
            sum1 += math.exp(F[i][k])
        total += (F[i][int(y[i])] - math.log(sum1))

    L = (-1 / n) * total / 10

    for i in range(dF.shape[0]):
        for j in range(dF.shape[1]):
            # indicator function
            if j == y[i]:
                indicator = 1
            else:
                indicator = 0

            numerator = math.exp(F[i][j])

            denominator = 0
            for k in range(3):
                denominator += math.exp(F[i][k])

            dF[i][j] = (-1 / n) * (indicator - (numerator / denominator)) / 10

    return L, dF
