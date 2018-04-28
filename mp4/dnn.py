# implement data acquisition and algorithm here
import numpy as np
import random as rand
from methods import *
from cache import *
import matplotlib.pyplot as plt
from tqdm import tqdm

def network(X, weights, biases, y, test=False):

    Z1, acache1 = affineForward(X, weights[0], biases[0])
    A1, rcache1 = reLUForward(Z1)

    Z2, acache2 = affineForward(A1, weights[1], biases[1])
    A2, rcache2 = reLUForward(Z2)

    Z3, acache3 = affineForward(A2, weights[2], biases[2])
    A3, rcache3 = reLUForward(Z3)

    F, acache4 = affineForward(A3, weights[3], biases[3])

    predict = np.zeros(y.shape)
    if test == True:
        for i in range(F.shape[0]):
            predict[i] = np.argmax(F[i])
        return predict

    loss, dF = crossEntropy(F, y)

    dA3, dW4, db4 = affineBackward(dF, acache4)
    dZ3 = reLUBackward(dA3, rcache3)

    dA2, dW3, db3 = affineBackward(dZ3, acache3)
    dZ2 = reLUBackward(dA2, rcache2)

    dA1, dW2, db2 = affineBackward(dZ2, acache2)
    dZ1 = reLUBackward(dA1, rcache1)

    dX, dW1, db1 = affineBackward(dZ1, acache1)

    # update parameters
    dWeights = [dW1, dW2, dW3, dW4]
    dBiases = [db1, db2, db3, db4]
    rate = 0.01

    for idx in range(len(weights)):
        weights[idx] = weights[idx] - rate * dWeights[idx]
        biases[idx] = biases[idx] - rate * dBiases[idx]

    return loss

def graphNet(eList, accList, lossList):

    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy', color=color)
    ax1.plot(eList, accList, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:red'
    ax2.set_ylabel('Loss', color=color)
    ax2.plot(eList, lossList, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.show()

def miniBatch(data, epoch, batch):

    weights, biases = weightsBiases((data.shape[1] - 1), 256, 256, 256, 3, 0.01)

    eList = []
    accList = []
    lossList = []

    for e in tqdm(range(epoch)):

        np.random.shuffle(data)
        epochLoss = 0

        for i in range(data.shape[0] / batch):

            X = data[(batch*i):(batch*i)+batch , 0:5]
            y = data[(batch*i):(batch*i)+batch , 5:6]

            loss = network(X, weights, biases, y)
            epochLoss += loss

        predict = network(data[:, 0:5], weights, biases, data[:, 5:6], True)
        acc = float(np.sum(predict == data[:, 5:6])) / data.shape[0]

        eList.append(e)
        accList.append(acc)
        lossList.append(epochLoss)

    graphNet(eList, accList, lossList)

    return

data = extract("expert_policy.txt")
miniBatch(data, 1000, 500)
