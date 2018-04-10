'''
Digit Classification with K_Nearest_Neighbors
Algorithm explained in the report
'''
import math
import sys
import numpy as np
from q2 import *
from collections import Counter
import operator


train_feats = []
train_labels = []
test_feats = []
test_labels = []

'''
Initialize training set from the file given
'''
def load_train_data(path):
    current_path = os.getcwd()
    global train_feats
    global train_labels

    with open(current_path + path) as infile:
        file_data = infile.read()


    temp = []
    for k in range(2436):
        for i in range(32):
            for j in range(32):
                temp.append(int(file_data[1059*k + 33*i + j]))
                if i == 31 and j == 31:
                    train_labels.append(int(file_data[1059*k + 33*i + j + 3]))
        train_feats.append(temp)
        temp = []

'''
Initialize test set from the file given
'''
def load_test_data(path):
    current_path = os.getcwd()
    global test_feats
    global test_labels

    with open(current_path + path) as infile:
        file_data = infile.read()


    temp = []
    for k in range(444):
        for i in range(32):
            for j in range(32):
                temp.append(int(file_data[1059*k + 33*i + j]))
                if i == 31 and j == 31:
                    test_labels.append(int(file_data[1059*k + 33*i + j + 3]))
        test_feats.append(temp)
        temp = []

'''
Similarity function used by K-Nearest-Neighbors
'''
def digit_score(train_feat, test_feat):
    return np.dot(train_feat, test_feat)

'''
K_Nearest_Neighbors Classification Algorithm
Process is explained in the report
'''
def knn_classify(train_feats, train_labels, test_feat, k):
    results = []
    for i in range(2436):
        score = digit_score(train_feats[i], test_feat)
        results.append((score, train_labels[i]))

    results = sorted(results, key = lambda x:x[0], reverse = True)
    return results[0:k]

'''
K_Nearest_Neighbors "main" function.
Calls on the classification function and generates an overall accuracy and
a confusion matrix
'''
def knn(train_feats, train_labels, test_feats, test_labels, k):
    count = 0
    conf_matrix = [[] for i in range(10)]
    num_feats = [0 for i in range(10)]
    for i in range(444):
        k_neighbors = []
        k_neighbor_labels = []
        k_neighbors = knn_classify(train_feats, train_labels, test_feats[i], k)
        for item in k_neighbors:
            k_neighbor_labels.append(item[1])
        counts = Counter(k_neighbor_labels)
        sorted_counts = sorted(counts.items(), key = operator.itemgetter(1), reverse = True)
        # print "actual " + str(test_labels[i])
        # print "predicted " + str(sorted_counts[0][0])
        if sorted_counts[0][0] == test_labels[i]:
            count += 1
        num_feats[test_labels[i]] += 1
        conf_matrix[test_labels[i]].append(sorted_counts[0][0])
        k_neighbors = []
        k_neighbor_labels = []

    print "knn: " + str(k) + ": " + str(count/(float(444)))
    for i in range(10):
        counts = Counter(conf_matrix[i])
        for j in counts.keys():
            print i, j, counts[j]/(float(num_feats[i]))

def main():
    load_train_data('/optdigits-orig_train.txt')
    load_test_data('/optdigits-orig_test.txt')

    knn(train_feats, train_labels, test_feats, test_labels, 3)

if __name__ == '__main__':
    main()
