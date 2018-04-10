# This file is going to be used for Part 1 of MP3

import numpy as np
from tqdm import tqdm
import math
import matplotlib.pyplot as plt
import sys

# Feature Extraction
'''
    Method: DataExtraction
    Inputs: filename -> Name of the file
    Outputs: features -> The features from the data
             labels -> The labels for each datum
    Description: This file takes the raw text and creates data that can be manipulated
'''
def DataExtraction(filename):

    file = open(filename, "r")

    features = []
    labels = []
    vector = np.zeros((32, 32))
    y = 0

    for line in tqdm(file):
        line = line.rstrip('\n')
        if len(line) == 32:
            text = list(line)
            for i in range(vector.shape[0]):
                vector[y][i] = int(text[i])
            y += 1
        elif len(line) != 32:
            text = line.split()
            for element in text:
                labels.append(int(element))
            features.append(vector)
            vector = np.zeros((32, 32))
            y = 0

    file.close()

    return features, labels

# Data Training
# - Clasifier goes here
'''
    Method: PriorDistribution
    Inputs: trainlabels -> The labels from the training data
    Outputs: priors -> The prior probability for each label
    Description: This method calculates the prior probability for each label
'''
def PriorDistribution(trainLabels):

    priors = np.zeros(10)

    for label in range(priors.shape[0]):
        count = 0.0
        for element in trainLabels:
            if element == label:
                count += 1
        priors[label] = count / len(trainLabels)

    return priors

'''
    Method: ConditionalProbability
    Inputs: trainData -> The training data
            trainlabels -> The training labels
            x -> The x component of current feature
            y -> The y component of current feature
            currClass -> The current class to calculate probability
            fVal -> The value of the feature to calculate
            k -> The smoothing constant
    Outputs: The conditional probability given a class for a certain feature
    Description: This method calculates the conditional probability given a class for a certain feature
'''
def ConditionalProbability(trainData, trainLabels, x, y, currClass, fVal, k):

    zeroCount = 0.0
    oneCount = 0.0

    for idx in range(len(trainLabels)):
        if trainLabels[idx] == currClass:
            if trainData[idx][x][y] == 0:
                zeroCount += 1
            elif trainData[idx][x][y] == 1:
                oneCount += 1

    prob0 = (zeroCount + k) / ((zeroCount + k) + (oneCount + k))
    prob1 = (oneCount + k) / ((zeroCount + k) + (oneCount + k))

    if fVal == 0:
        return prob0
    else:
        return prob1

'''
    Method: CondProbMatrix
    Inputs: trainData -> training data
            trainLabels -> training labels
            k -> Smoothing constant
    Outputs: mat -> The matrix containing all prior conditional probabilities
    Description: This method optimizes the training process and makes the classification time faster
'''
def CondProbMatrix(trainData, trainLabels, k):

    mat = np.zeros((10, 2048))

    for label in tqdm(range(mat.shape[0])):
        for x in range(32):
            for y in range(32):
                mat[label][(32 * x) + y] = ConditionalProbability(trainData, trainLabels, x, y, label, 0, k)
        for x in range(32):
            for y in range(32):
                mat[label][(32 * x) + y + 1024] = ConditionalProbability(trainData, trainLabels, x, y, label, 1, k)

    return mat

'''
    Method: NaiveBayes
    Inputs: data -> the data to run classifier on
            labelArrSize -> Size of the label array
            priors -> parameter estimates from TRAINING
            mat -> parameter estimates from Training
    Outputs: estimatedLabels -> The estimated labels from the classifier
    Description: This method runs the Naive Bayes algorithm on a test data set and returns the classifiers labels
'''
def NaiveBayes(data, labelArrSize, priors, mat):

    estimatedLabels = np.zeros(labelArrSize)
    temp = np.zeros(10)

    for idx in tqdm(range(len(data))):
        datum = data[idx]
        for label in range(10):
            tempSum = 0.0
            tempSum += math.log(priors[label])
            for x in range(datum.shape[0]):
                for y in range(datum.shape[1]):
                    if(datum[x][y] == 0):
                        tempSum += math.log(mat[label][(32 * x) + y])
                    else:
                        tempSum += math.log(mat[label][(32 * x) + y + 1024])
            temp[label] = tempSum
        estimatedLabels[idx] = np.argmax(temp)
        # print "Finished datum number", idx, "out of", len(data) - 1
        temp = np.zeros(10)

    return estimatedLabels

'''
    Method: ConfMatrix
    Inputs: estimatedLabels -> estimated labels from classifier
            trueLabels -> true labels from data set
    Outputs: mat -> The confusion matrix
    Description: This method creates a confusion matrix from the classifier data
'''
def ConfMatrix(estimatedLabels, trueLabels):

    mat = np.zeros((10, 10))
    denomCount = 0.0

    for row in range(mat.shape[0]):
        for idx in range(len(trueLabels)):
            if trueLabels[idx] == row:
                denomCount += 1
        for col in range(mat.shape[1]):
            numCount = 0.0
            for idx in range(len(trueLabels)):
                if trueLabels[idx] == row:
                    if estimatedLabels[idx] == col:
                        numCount += 1
            mat[row][col] = numCount / denomCount
        denomCount = 0.0

    print "CONFUSION MATRIX"
    for row in range(mat.shape[0]):
        print "############", "CLASS", row, "############"
        for col in range(mat.shape[1]):
            print "Label", col, "=", mat[row][col]

    print
    return mat

'''
    Method: ClassifierAccuracy
    Inputs: estimatedLabels -> The estimated labels from the classifier
            trueLabels -> The true labels from the data set
            confMat -> The confusion matrix
    Outputs: None
    Description: This method calculates the accuracy for each label
'''
def ClassifierAccuracy(estimatedLabels, trueLabels, confMat):

    count = 0.0

    for idx in range(len(estimatedLabels)):
        if estimatedLabels[idx] == trueLabels[idx]:
            count += 1

    for x in range(confMat.shape[0]):
        for y in range(confMat.shape[1]):
            if x == y:
                print "DIGIT", x, "ACCURACY:", confMat[x][y]

    print "OVERALL ACCURACY:", (count/len(estimatedLabels))

    return

'''
    Method: OddsRatio
    Inputs: mat -> the prior probability matrix
            label1 -> one of the digits
            label2 -> the second of the pair of digits
    Outputs: None
    Description: Prints the likelihood ratios and odds ratios for each pair of digits
'''
def OddsRatio(mat, label1, label2):

    likelihoods1 = np.zeros((32, 32))
    likelihoods2 = np.zeros((32, 32))
    oddsRatio = np.zeros((32, 32))

    for x in range(likelihoods1.shape[0]):
        for y in range(likelihoods2.shape[1]):
            likelihoods1[x][y] = mat[label1][(32 * x) + y + 1024]
            likelihoods2[x][y] = mat[label2][(32 * x) + y + 1024]
            oddsRatio[x][y] = likelihoods1[x][y] / likelihoods2[x][y]

            likelihoods1[x][y] = math.log(likelihoods1[x][y])
            likelihoods2[x][y] = math.log(likelihoods2[x][y])
            oddsRatio[x][y] = math.log(oddsRatio[x][y])


    plt.imshow(likelihoods1, cmap='jet')
    fname = "likelyhood_" + str(label1)
    plt.savefig(fname)

    plt.imshow(likelihoods2, cmap='jet')
    fname = "likelyhood_" + str(label2)
    plt.savefig(fname)

    plt.imshow(oddsRatio, cmap='jet')
    fname = "OddsRatio_" + str(label1) + "_" + str(label2)
    plt.savefig(fname)

    return

# Data Testing

# Classifier Evaluation
# - Confusion Matrix
# - Odds Ratios

def main():

    print "DATA EXTRACTION"
    trainData, trainLabels = DataExtraction("optdigits-orig_train.txt")
    testData, testLabels = DataExtraction("optdigits-orig_test.txt")

    print "TRAINING DATA"
    priors = PriorDistribution(trainLabels)
    mat = CondProbMatrix(trainData, trainLabels, int(sys.argv[1]))

    print "RUNNING CLASSIFIER"
    estimatedLabels = NaiveBayes(testData, len(testLabels), priors, mat)

    confMat = ConfMatrix(estimatedLabels, testLabels)
    ClassifierAccuracy(estimatedLabels, testLabels, confMat)

    OddsRatio(mat, 4, 7)
    OddsRatio(mat, 2, 8)
    OddsRatio(mat, 9, 3)
    OddsRatio(mat, 5, 9)

if __name__ == "__main__":
    main()
