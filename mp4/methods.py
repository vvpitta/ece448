# This file will be for all the functions for dnn
import numpy as np
import random as rand
import math

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

# ADD ONE MORE LAYER
def weightsBiases(d, d1, d2, d3, parameter):

    w_1 = np.zeros((d, d1))
    w_2 = np.zeros((d1, d2))
    w_3 = np.zeros((d2, d3))
    w_4 = np.zeros((d3, 3))

    b_1 = np.zeros(d1)
    b_2 = np.zeros(d2)
    b_3 = np.zeros(d3)
    b_4 = np.zeros(3)

    for mat in [w_1, w_2, w_3, w_4]:
        for x in range(mat.shape[0]):
            for y in range(mat.shape[1]):
                mat[x][y] = round(rand.uniform(0.01, 1), 3) * parameter

    return [w_1, w_2, w_3, w_4], [b_1, b_2, b_3, b_4]

def affineForward(A, W, b):

    Z = np.dot(A, W) + b
    cache = AffineCache(A, W, b)

    return Z, cache

def reLUForward(Z):

    A = Z
    # Zchange = np.zeros((A.shape[0], A.shape[1]))
    Zchange = np.zeros(A.shape)

    for x in range(A.shape[0]):
        for y in range(A.shape[1]):
            if(A[x][y] < 0):
                A[x][y] = 0
                Zchange[x][y] = 1

    cache = ReLUCache(Z, Zchange)

    return A, cache

def affineBackward(dZ, cache):

    A, W, b = cache.getAll()
    # dA = np.zeros((A.shape[0], A.shape[1]))
    # dW = np.zeros((W.shape[0], W.shape[1]))
    # db = np.zeros(b.shape[0])
    dA = np.zeros(A.shape)
    dW = np.zeros(W.shape)
    db = np.zeros(b.shape)

    for x in range(dA.shape[0]):
        for y in range(dA.shape[1]):
            dA[x][y] = np.dot(dZ[x,:], W[y,:])
            # tempSum = 0
            # for j in range(dZ.shape[1]):
            #     tempSum += (dZ[x][j] * W[y][j])
            # dA[x][y] = tempSum

    for x in range(dW.shape[0]):
        for y in range(dW.shape[1]):
            dW[x][y] = np.dot(A[:,x], dZ[:,y])
            # tempSum = 0
            # for i in range(A.shape[0]):
            #     tempSum += (A[i][x] * dZ[i][y])
            # dW[x][y] = tempSum

    for x in range(db.shape[0]):
        db[x] = np.sum(dZ[:,x])
        # tempSum = 0
        # for i in range(dZ.shape[0]):
        #     tempSum += dZ[i][x]
        # db[x] = tempSum

    return dA, dW, db

def reLUBackward(dA, cache):

    Z, Zchange = cache.getAll()

    dZ = dA

    for x in range(Zchange.shape[0]):
        for y in range(Zchange.shape[1]):
            if Zchange[x][y] == 1:
                dZ[x][y] = 0

    return dZ

def crossEntropy(F, y):

    n = F.shape[0]
    dF = np.zeros(F.shape)

    total = 0
    for i in range(F.shape[0]):
        sum1 = 0
        for k in range(3):
            sum1 += math.exp(F[i][k])
        total += (F[i][y[i]] - math.log(sum1))

    L = (-1 / n) * total

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

            dF[i][j] = (-1 / n) * (indicator - (numerator / denominator))

    return L, dF
