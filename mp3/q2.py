'''
Digit classification with multi-class perceptron
'''
import os
import sys
import numpy as np


train_feats = []
train_labels = []
test_feats = []
test_labels = []

def output_to_terminal(output_vec):
    output = []
    for i in range(len(output_vec)):
        if (i+1)%32 == 0 and i != 0:
            output.append(str(output_vec[i]))
            output.append("\n")
        else:
            output.append(str(output_vec[i]))

    output_string = ''.join(output)

    print output_string
#######################################################################
def activation_fn(feature_vec, digit_vec):
    scores = []

    for i in range(len(digit_vec)):
        score = np.dot(feature_vec, digit_vec[i])
        scores.append(score)

    np_scores = np.asarray(scores)
    return np.argmax(np_scores)

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


def initialize_digit_vecs():
    empty_vec = [0 for i in range(1024)]
    digit_vecs = []

    for i in range(10):
        digit_vecs.append(empty_vec)

    return digit_vecs

def perceptron_train(digit_vecs):
    global train_feats
    global train_labels
    digit_vecs_new = []
    print len(digit_vecs), len(digit_vecs[0])
    for i in range(10):
        temp = []
        for j in range(1024):
            temp.append(digit_vecs[i][j])
        digit_vecs_new.append(temp)

    for i in range(2436):
        label = activation_fn(train_feats[i], digit_vecs)
        if label != train_labels[i]:
            # output_to_terminal(train_feats[i])
            for j in range(1024):
                digit_vecs_new[label][j] = (digit_vecs_new[label][j] - train_feats[i][j])
#                print digit_vecs[label][j], train_feats[i][j], digit_vecs[label][j-1]
                digit_vecs_new[train_labels[i]][j] = (digit_vecs_new[train_labels[i]][j] + train_feats[i][j])
#                print digit_vecs[train_labels[i]][j], train_feats[train_labels[i]][j]
    return digit_vecs_new

def perceptron_test(digit_vecs):
    global test_feats
    global test_labels
    count = 0

    for i in range(444):
        label = activation_fn(test_feats[i], digit_vecs)
        print "actual " + str(test_labels[i])
        print "predicted " + str(label)
        if label == test_labels[i]:
            count += 1

    print count/(float(444))

def main():
    load_train_data('/optdigits-orig_train.txt')
    load_test_data('/optdigits-orig_test.txt')

    digit_vecs = initialize_digit_vecs()

    digit_vecs = perceptron_train(digit_vecs)

    perceptron_test(digit_vecs)

    # output_to_terminal(digit_vecs[7])
    # print digit_vecs






if __name__ == '__main__':
    main()