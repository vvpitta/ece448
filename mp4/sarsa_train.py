'''
Sarsa Training
'''

# This file will be used to test the pong agent

from pong import *
from qLearning import *
from sarsa_learn import *
import random as rand
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
from simulation import *
import numpy as np

s = slearn()
# currState = PongState(0.5, 0.5, 0.03, 0.01, 0.4)
# currTuple = currState.getState()
# curr_key = currState.discreteMap()
tot_hits = []

for i in tqdm(range(100000)):
    # ballX = 0.5
    # ballY = 0.5
    vX = round(rand.random(), 2)
    while vX < 0.06:
        vX = round(rand.random(), 2)
    if i%2 == 0:
        vX *= -1
    # vY = round(rand.uniform(-0.03, 0.03), 3)
    # paddle = 0.4
    #
    # currState = PongState(ballX, ballY, vX, vY, paddle)
    currState = PongState(0.5, 0.5, vX, 0.01, 0.4)
    currTuple = currState.getState()
    curr_key = currState.discreteMap()
    reward = 0
    hits = 0

    if i % 10000 == 0 and i != 0:
        print
        print 'Averaging ', sum(tot_hits)/len(tot_hits), ' hit(s) by game ', i

    while reward != -1:
        # action, index = currState.chooseAction()
        # print 'Action:', action, 'Index:', index

        actions = [0, 0.04, -0.04]
        s.add_to_state(curr_key)
        action_c_scores = s.get_actions(curr_key)
        if rand.random() < 0.05:
            index = rand.randint(0,2)
            value = action_c_scores[index]
        else:
            value, index = max(action_c_scores), np.argmax(action_c_scores)
        reward = currState.moveNextStep(actions[index])
        next_key = currState.discreteMap()
        action_q_scores = s.get_actions(next_key)
        if rand.random() < 0.05:
            index = rand.randint(0,2)
            future_val = action_q_scores[index]
        else:
            future_val = max(action_q_scores)
        # print 'Reward:', reward

        # print initialState.getState()
        # print curr_key
        # print next_key

        # (50/(50+(q.seen_val(curr_key))))

        new_value = value + (50/float((50+(s.seen_val(curr_key))))) * (reward + 0.8*future_val - value)
        # print "Value:", value

        s.set_s(curr_key, index, new_value)

        curr_key = next_key
        # print
        if reward == 1:
            hits += 1

    tot_hits.append(hits)


s_dict = s.get_smat()
ss_dict = {}
string_object_mapping = {}
i = 0
for key in q_dict.keys():
    state = "state" + str(i)
    string_object_mapping[state] = key
    ss_dict[state] = s_dict[key]
    i += 1

with open('smat.txt', 'w') as file:
    file.write(json.dumps(ss_dict))

with open('string_object_map_s.txt', 'w') as file2:
    file2.write(json.dumps(string_object_mapping))

x_plot = []
y_plot = []
x_char_plot = []
y_char_plot = []

for i in range(len(x_plot)):
    x_char_plot.append(str(x_plot[i]))
    y_char_plot.append(str(y_plot[i]))

x_string = ''.join(x_char_plot)
y_string = ''.join(y_char_plot)

with open('sarsa_x', 'w') as file3:
    file3.write(x_string)

with open('sarsa_y', 'w') as file4:
    file4.write(y_string)

for i in range(len(tot_hits)):
    if i == 0:
        x_plot.append(i)
        y_plot.append(sum(tot_hits[0:i]))
    else:
        x_plot.append(i)
        y_plot.append(sum(tot_hits[0:i])/float(i))


plt.plot(x_plot, y_plot)
plt.ylabel("Mean Reward Per Episode")
plt.xlabel("Episode")
plt.title("Mean Reward Per Episode vs Episode")
plt.savefig("sarsa.png")
