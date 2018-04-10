# This file is the second implmentation of ExtraCredit 1.2

import numpy as np
from tqdm import tqdm
import math
import itertools

# Feature Extraction

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

# prior distribution
def PriorDistribution(trainLabels):

    priors = np.zeros(10)

    for label in range(priors.shape[0]):
        count = 0.0
        for element in trainLabels:
            if element == label:
                count += 1
        priors[label] = count / len(trainLabels)

    return priors

# Likelihood Estimation
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

    mat = np.zeros((10, 2048))

    for label in tqdm(range(mat.shape[0])):
        for x in range(32):
            for y in range(32):
                mat[label][(32 * x) + y] = ConditionalProbability(trainData, trainLabels, x, y, label, 0)
        for x in range(32):
            for y in range(32):
                mat[label][(32 * x) + y + 1024] = ConditionalProbability(trainData, trainLabels, x, y, label, 1)

    return mat

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

#Extra Credit Starts Here
'''
Creates a dictionary of all the distinct features given the size of the patch
Creates a list of all the distinct features given the size of the patch
'''
def featurelist(n,m):
    size = n*m
    distinctfeatures = list(itertools.product([0,1], repeat = size))
    allfeatures = {}
    for i in range(len(distinctfeatures)):
		allfeatures[tuple(distinctfeatures[i])] = i
    return distinctfeatures, allfeatures

'''
This method is not used for training or testing in this implmentation
'''
def ecConditionalProbability(trainData, trainLabels, x, y, currClass, overlap, featuretocheck, extractedfeatures, n, m):
   # count = [len(allfeatures)]
    zeroCount = 0
    oneCount = 0
    for idx in range(len(trainLabels)):
        if trainLabels[idx] == currClass:
            row1 = extractedfeatures[x][0] 
            col1 = extractedfeatures[x][1]
            a = makefeature(trainData, row1, col1, n, m, idx)
            count = compare(featuretocheck, a)
            if count == 1:
                oneCount += 1
            else:
                zeroCount += 1

    ##prob0 = (zeroCount + 10) / ((zeroCount + 10) + (oneCount + 10))
    prob1 = (oneCount + 10.0) / ((zeroCount + 10.0) + (oneCount + 10.0))
    #print str(zeroCount+10.0+oneCount+10.0)
    #print oneCount
    #print prob1
    return (prob1)

'''
This method is not used for training or testing in this implmentation
'''
def compare(comp1, comp2):
    for i in range(len(comp1)):
        if comp1[i] != comp2[i]:
            return 0
    return 1

'''
Used to find the patch given the data and the starting coordinates of the patch and size of the patch
'''
def makefeature(trainData, x, y, n, m, idx):
    a = []
    for i in range(n):
        for j in range(m):
          a.append(trainData[idx][x+i][y+j])
    return a
'''
returns a list of all the starting points of all possible patches given a patch and whether the patch is overlapping is not or not
'''
def featureExtract(n,m,overlap):
    a = []
    i = 0
    j = 0
    if overlap:
        while i < (32-(n-1)):
            j=0
            while j <(32-(m-1)):
                a.append([i,j])
                j+=1
            i+=1
    else:
        while i < 32:
            j = 0
            while j < 32:
                #print str(i) + "," + str(j)
                a.append([i,j])
                j+=m
            i+=n
    return a
    '''elif overlap == True:
        while i <'''

# generate the Conditional Probability Matrix for feature sets given the training data, size of the feature, overlapping or disjoint, starting point of all possible patches for a 32*32 image, dicitionary of all possible features
def ecCondProbMatrix(trainData, trainLabels, n,m,overlap,extractedfeatures, allfeatures):
    depth = 2**(n*m)
    col = len(extractedfeatures)
    mat = np.zeros((10,col, depth))
    lenlabels = np.zeros(10)
    for label in tqdm(range(10)):
        #print "*"
        for x in range(len(extractedfeatures)):
            #print "col:" + str(x)
            count = 0
            for idx in range(len(trainLabels)):

                if(trainLabels[idx] == label):
                    #lenlabels[label] = lenlabels[label] + 1.0
                    #print "reached"
                    count += 1
                    row1 = extractedfeatures[x][0]
                    col1 = extractedfeatures[x][1]
                    a = makefeature(trainData, row1, col1, n, m, idx)
                    y = allfeatures[tuple(a)]
                    mat[label][x][y] = mat[label][x][y] + 1.0
            lenlabels[label] = count
           
    #print lenlabels
    return mat, lenlabels

'''
Method to compare two floats 
'''
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

# NaiveBayes Classifier mainly given the priors and the conditional probability matrix
def ecNaiveBayes(data, labelArrSize, priors, mat, extractedfeatures, n, m, allfeatures, lenlabels):

    estimatedLabels = np.zeros(labelArrSize)
    temp = np.zeros(10)
    for idx in tqdm(range(len(data))):
        #datum = data[idx]
        for label in range(10):
            tempSum = 0.0
            tempSum += math.log(priors[label])
            for c in range(len(extractedfeatures)):
                row1 = extractedfeatures[c][0]
                col1 = extractedfeatures[c][1]
                a = makefeature(data, row1, col1, n, m, idx)
                y = allfeatures[tuple(a)]
                mat[label][c][y] = ((mat[label][c][y])/(lenlabels[label])) + 0.00001
                tempSum += math.log(mat[label][c][y])

            temp[label] = tempSum
        estimatedLabels[idx] = np.argmax(temp)
        temp = np.zeros(10)

    return estimatedLabels

# Data Testing

# Classifier Evaluation
# - Confusion Matrix
# - Odds Ratios


print "DATA EXTRACTION"
trainData, trainLabels = DataExtraction("optdigits-orig_train.txt")
testData, testLabels = DataExtraction("optdigits-orig_test.txt")
#print len(trainLabels)

print "TRAINING DATA"
priors = PriorDistribution(trainLabels)

##mat = CondProbMatrix(trainData, trainLabels)
distinctfeatures, allfeatures = featurelist(4,4)
#print str(allfeatures[(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)])
#print "allfeatures"
#print allfeatures
extractedfeatures = featureExtract(4,4,True)
#print "extractedfeatures"
#print extractedfeatures
#print len(extractedfeatures)

mat, lenlabels = ecCondProbMatrix(trainData, trainLabels,4, 4, True, extractedfeatures, allfeatures)
#print mat[0][0]

print "RUNNING CLASSIFIER"
##estimatedLabels = NaiveBayes(testData, len(testLabels), priors, mat)
estimatedLabels = ecNaiveBayes(testData, len(testLabels), priors, mat, extractedfeatures, 4, 4, allfeatures, lenlabels)
#print estimatedLabels
confMat = ConfMatrix(estimatedLabels, testLabels)
ClassifierAccuracy(estimatedLabels, testLabels, confMat)

