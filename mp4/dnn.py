# implement data acquisition and algorithm here
import numpy as np
import random as rand
from methods import *
from cache import *
from pong import *
import matplotlib.pyplot as plt
from tqdm import tqdm

'''
    Method: network
    Inputs: Arrays for testing/training
    Outputs: classifications or loss
    Description: This method implements the actual neural network
'''
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

'''
    Method: testGame
    Inputs: Arrays for modification
    Outputs: Return output for affine forward
    Description: This function tests the net on the game
'''
def testGame(state, weights, biases):

    Z1, acache1 = affineForward(state, weights[0], biases[0])
    A1, rcache1 = reLUForward(Z1)

    Z2, acache2 = affineForward(A1, weights[1], biases[1])
    A2, rcache2 = reLUForward(Z2)

    Z3, acache3 = affineForward(A2, weights[2], biases[2])
    A3, rcache3 = reLUForward(Z3)

    F, acache4 = affineForward(A3, weights[3], biases[3])

    return np.argmax(F)

'''
    Method: graphNet
    Inputs: Arrays for modification
    Outputs: Return output for affine forward
    Description: This method graphs the loss and accuracy vs. epoch number
'''
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

    return

'''
    Method: play_game
    Inputs: Arrays for modification
    Outputs: Return output for affine forward
    Description: This method plays the game
'''
def play_game(weights, biases):

    hits = 0
    currState = PongState(0.5, 0.5, 0.03, 0.01, 0.4)
    curr_key = np.asarray(currState.getState())
    paddle_actions = [0.04, 0, -0.04]

    while True:

        action_idx = testGame(curr_key, weights, biases)
        action = paddle_actions[action_idx]
        reward = currState.moveNextStep(action)
        next_key = np.asarray(currState.getState())

        if reward == -1:
            return hits
        if reward == 1:
            hits += 1
        curr_key = next_key

'''
    Method: confMat
    Inputs: Arrays for modification
    Outputs: Return output for affine forward
    Description: This method creates the confusion matrix for the classifier
'''
def ConfMat(data, weights, biases):

    predict = network(data[:, 0:5], weights, biases, data[:, 5:6], True)
    zeros = np.sum(data[:, 5:6] == 0)
    ones = np.sum(data[:, 5:6] == 1)
    twos = np.sum(data[:, 5:6] == 2)
    confMat = np.zeros((3,3))

    for idx in range(predict.shape[0]):
        if(data[idx][5] == 0):
            if(predict[idx] == 0):
                confMat[0][0] += 1
            elif(predict[idx] == 1):
                confMat[0][1] += 1
            else:
                confMat[0][2] += 1
        elif(data[idx][5] == 1):
            if(predict[idx] == 0):
                confMat[1][0] += 1
            elif(predict[idx] == 1):
                confMat[1][1] += 1
            else:
                confMat[1][2] += 1
        else:
            if(predict[idx] == 0):
                confMat[2][0] += 1
            elif(predict[idx] == 1):
                confMat[2][1] += 1
            else:
                confMat[2][2] += 1

    for x in range(confMat.shape[0]):
        for y in range(confMat.shape[1]):
            if x == 0:
                confMat[x][y] = float(confMat[x][y]) / zeros
            elif x == 1:
                confMat[x][y] = float(confMat[x][y]) / ones
            else:
                confMat[x][y] = float(confMat[x][y]) / twos

    return confMat

'''
    Method: miniBatch
    Inputs: Arrays for modification
    Outputs: Return output for affine forward
    Description: This method acts as the main function for initializing/training/testing the neural net
'''
def miniBatch(data, epoch, batch):

    weights, biases = weightsBiases((data.shape[1] - 1), 256, 256, 256, 3, 0.01)

    eList = []
    accList = []
    lossList = []
    highestAcc = 0

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
        if(acc > highestAcc):
            highestAcc = acc

        eList.append(e)
        accList.append(acc)
        lossList.append(epochLoss)

    print highestAcc
    confMat = ConfMat(data, weights, biases)
    print confMat

    hits_tot = []
    for i in range(200):
        hits = play_game(weights, biases)
        hits_tot.append(hits)

    print "Average hits:" , sum(hits_tot)/2

    graphNet(eList, accList, lossList)

    return


'''
    Call miniBatch
'''
data = extract("expert_policy.txt")
miniBatch(data, 1000, 500)
