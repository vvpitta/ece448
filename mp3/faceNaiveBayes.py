# this file is for extra credit

import numpy as np
from tqdm import tqdm
import math
import matplotlib.pyplot as plt

def FaceData(datafile, labelfile):

    features = []
    labels = []
    vector = np.zeros((70, 60))
    y = 0

    file = open(datafile, "r")
    lines = file.readlines()

    for idx in tqdm(range(len(lines))):
        line = lines[idx].rstrip('\n')
        text = list(line)
        if(idx % 70 == 0 and idx != 0):
            features.append(vector)
            vector = np.zeros((70, 60))
            y = 0
        for i in range(vector.shape[1]):
            if text[i] == '#':
                vector[y][i] = 1
            else:
                vector[y][i] = 0
        if(idx == len(lines) - 1):
            features.append(vector)
        y += 1

    file.close()

    file = open(labelfile, "r")

    lines = file.readlines()
    for idx in range(len(lines)):
        line = lines[idx].rstrip('\n')
        labels.append(int(line))

    file.close()

    return features, labels

def PriorDistribution(trainLabels):

    priors = np.zeros(2)

    for label in range(priors.shape[0]):
        count = 0.0
        for element in trainLabels:
            if element == label:
                count += 1
        priors[label] = count / len(trainLabels)

    return priors

def ConditionalProbability(trainData, trainLabels, x, y, currClass, fVal):

    zeroCount = 0.0
    oneCount = 0.0

    for idx in range(len(trainLabels)):
        if trainLabels[idx] == currClass:
            if trainData[idx][x][y] == 0:
                zeroCount += 1
            elif trainData[idx][x][y] == 1:
                oneCount += 1

    prob0 = (zeroCount + 10) / ((zeroCount + 10) + (oneCount + 10))
    prob1 = (oneCount + 10) / ((zeroCount + 10) + (oneCount + 10))

    if fVal == 0:
        return prob0
    else:
        return prob1

def CondProbMatrix(trainData, trainLabels):

    mat = np.zeros((2, 8400))

    for label in tqdm(range(mat.shape[0])):
        for x in range(70):
            for y in range(60):
                mat[label][(60 * x) + y] = ConditionalProbability(trainData, trainLabels, x, y, label, 0)
        for x in range(70):
            for y in range(60):
                mat[label][(60 * x) + y + 4200] = ConditionalProbability(trainData, trainLabels, x, y, label, 1)

    return mat

def NaiveBayes(data, labelArrSize, priors, mat):

    estimatedLabels = np.zeros(labelArrSize)
    temp = np.zeros(2)

    for idx in tqdm(range(len(data))):
        datum = data[idx]
        for label in range(2):
            tempSum = 0.0
            tempSum += math.log(priors[label])
            for x in range(datum.shape[0]):
                for y in range(datum.shape[1]):
                    if(datum[x][y] == 0):
                        tempSum += math.log(mat[label][(60 * x) + y])
                    else:
                        tempSum += math.log(mat[label][(60 * x) + y + 4200])
            temp[label] = tempSum
        estimatedLabels[idx] = np.argmax(temp)
        # print "Finished datum number", idx, "out of", len(data) - 1
        temp = np.zeros(2)

    return estimatedLabels

def ClassifierAccuracy(estimatedLabels, trueLabels):#, confMat):

    count = 0.0

    for idx in range(len(estimatedLabels)):
        if estimatedLabels[idx] == trueLabels[idx]:
            count += 1

    # for x in range(confMat.shape[0]):
    #     for y in range(confMat.shape[1]):
    #         if x == y:
    #             print "DIGIT", x, "ACCURACY:", confMat[x][y]

    print "OVERALL ACCURACY:", (count/len(estimatedLabels))

    return

def main():

    print "DATA EXTRACTION"
    trainData, trainLabels = FaceData("facedatatrain", "facedatatrainlabels")
    testData, testLabels = FaceData("facedatatest", "facedatatestlabels")

    print "TRAINING DATA"
    priors = PriorDistribution(trainLabels)
    mat = CondProbMatrix(trainData, trainLabels)

    print "RUNNING CLASSIFIER"
    estimatedLabels = NaiveBayes(testData, len(testLabels), priors, mat)
    ClassifierAccuracy(estimatedLabels, testLabels)#, confMat)

if __name__ == "__main__":
    main()
