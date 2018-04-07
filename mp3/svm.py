'''
SVC classifier (LinearSVC)
'''
from sklearn.svm import LinearSVC
import os
import sys
from q2 import *

train_feats = []
train_labels = []
test_feats = []
test_labels = []

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


def main():
    load_train_data('/optdigits-orig_train.txt')
    load_test_data('/optdigits-orig_test.txt')

    model = LinearSVC(random_state = 0)
    model = model.fit(train_feats, train_labels)
    y_pred = model.predict(test_feats)
    count = 0
    for i in range(len(y_pred)):
        if y_pred[i] == test_labels[i]:
            count += 1

    print count/(float(444))




if __name__ == "__main__":
    main()
