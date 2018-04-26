'''
simulation of games
'''

from pong import *
from qLearning import *
import math
import random as rand
import json
import os
import numpy as np

def play_game(q):
    hits = 0
    currState = PongState(0.5, 0.5, 0.03, 0.01, 0.4)
    curr_key = currState.discreteMap()
    paddle_actions = [0, 0.04, -0.04]
    while True:
        action_idx = np.argmax(q.get_actions(curr_key))
        action = paddle_actions[action_idx]
        print "currState", currState.getState()
        print "dmap", currState.discreteMap()
        print "action", action
        reward = currState.moveNextStep(action)
        print "reward", reward
        next_key = currState.discreteMap()
        if reward == -1:
            return hits
        if reward == 1:
            hits += 1
        curr_key = next_key
        print


def main():
    q = qlearn()
    current_path = os.getcwd()
    path1 = "/qmat.txt"
    path2 = "/string_object_map.txt"

    som = {}
    vals = {}
    qmat = {}

    with open(current_path + path1) as file1:
        vals = json.loads(file1.read())

    with open(current_path + path2) as file2:
        som = json.loads(file2.read())

    for key in som.keys():
        tup = (som[key][0], som[key][1], som[key][2], som[key][3], som[key][4])
        qmat[tup] = vals[key]

    q.set_qmat(qmat)
    hits_tot = []
    for i in range(5):
        hits = play_game(q)
        hits_tot.append(hits)

    print
    print hits_tot







if __name__ == '__main__':
    main()
