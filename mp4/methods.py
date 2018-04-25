# This file will be for all the functions for dnn
import numpy as np
import random as rand

def extract(filename):

    file = open(filename, 'r')

    data = np.zeros((10000, 5))
    targets = np.zeros(10000)
    i = 0

    for line in file:
        line = line.split()
        for idx in range(len(line)):
            line[idx] = float(line[idx])
        data[i] = line[0:5]
        targets[i] = line[5]
        i += 1

    file.close()

    return data, targets

def weightsBiases(d, d1, d2, parameter):

    w_1 = np.zeros((d, d1))
    w_2 = np.zeros((d, d2))
    w_3 = np.zeros((d, 3))

    b_1 = np.zeros(d1)
    b_2 = np.zeros(d2)
    b_3 = np.zeros(3)

    for mat in [w_1, w_2, w_3]:
        for x in range(mat.shape[0]):
            for y in range(mat.shape[1]):
                mat[x][y] = round(rand.uniform(0.01, 1), 3) * parameter

    return w_1, w_2, w_3, b_1, b_2, b_3

def affineForward(A, W, b):

    Z = np.dot(A, W) + b
    cache = AffineCache(A, W, b)

    return Z, cache

def reLUForward(Z):

    A = Z
    Zchange = np.zeros((A.shape[0], A.shape[1]))

    for x in range(A.shape[0]):
        for y in range(A.shape[1]):
            if(A[x][y] < 0):
                A[x][y] = 0
                Zchange[x][y] = 1

    cache = ReLUCache(Z, Zchange)

    return A, cache

def affineBackward(dZ, cache):

    A, W, b = cache.getAll()


    return

def reLUBackward():
    return

def crossEntropy():
    return
