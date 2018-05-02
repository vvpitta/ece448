# This file will be used to test the pong agent

from pong import *
from qLearning import *
import random as rand
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
from simulation import *
import numpy as np

q = qlearn()

# Initiliazing the Q Matrix with 0s for every state
init_mat = {}
seen_state = {}
x_vels = [-1,1]
for ballX in range(13):
    for ballY in range(13):
        for vX in x_vels:
            for vY in range(-1,2):
                for paddle in range(12):
                    init_mat[(ballX, ballY, vX, vY, paddle)] = [0.0, 0.0, 0.0]
                    seen_state[(ballX, ballY, vX, vY, paddle)] = 0
init_mat[(12,0,0,0,0)] = [0.0, 0.0, 0.0]
seen_state[(12,0,0,0,0)] = 0
q.set_qmat(init_mat)
q.set_seenMat(seen_state)
tot_hits = []


# Training 100k times
for i in tqdm(range(100000)):
    # ballX = 0.5
    # ballY = 0.5
    vX = round(rand.random(), 2)
    while vX < 0.06:
        vX = round(rand.random(), 2)
    if i%2 == 0:
        vX *= -1


    # Initial ball state for every game
    currState = PongState(0.5, 0.5, vX, 0.01, 0.4)
    currTuple = currState.getState()
    curr_key = currState.discreteMap()
    reward = 0
    hits = 0

    if i % 10000 == 0 and i != 0:
        print
        print 'Averaging ', sum(tot_hits)/len(tot_hits), ' hit(s) by game ', i

    # Play the game till the AI loses
    while reward != -1:

        actions = [0, 0.04, -0.04]
        q.add_to_state(curr_key)
        action_c_scores = q.get_actions(curr_key)

        # Exploration function to choose a random action or the
        # action that leads to the max value for a specific state
        if rand.random() < 0.05:
            index = rand.randint(0,2)
            value = action_c_scores[index]
        else:
            value, index = max(action_c_scores), np.argmax(action_c_scores)

        # Go to next state and pick corresponding action with the largest score
        reward = currState.moveNextStep(actions[index])
        next_key = currState.discreteMap()
        action_q_scores = q.get_actions(next_key)
        future_val = max(action_q_scores)


        # Bellman Algorithm to update Q value for current state
        new_value = value + (50/float((50+(q.seen_val(curr_key))))) * (reward + 0.8*future_val - value)
        # print "Value:", value

        q.set_q(curr_key, index, new_value)

        curr_key = next_key
        # print
        if reward == 1:
            hits += 1

    tot_hits.append(hits)



# Save and plot training results
q_dict = q.get_qmat()
qs_dict = {}
string_object_mapping = {}
i = 0
for key in q_dict.keys():
    state = "state" + str(i)
    string_object_mapping[state] = key
    qs_dict[state] = q_dict[key]
    i += 1

with open('qmat_new.txt', 'w') as file:
    file.write(json.dumps(qs_dict))

with open('string_object_map_new.txt', 'w') as file2:
    file2.write(json.dumps(string_object_mapping))

x_plot = []
y_plot = []


for i in range(len(tot_hits)):
    if i == 0:
        x_plot.append(i)
        y_plot.append(sum(tot_hits[0:i]))
    else:
        x_plot.append(i)
        y_plot.append(sum(tot_hits[0:i])/float(i))


x_char_plot = []
y_char_plot = []

for i in range(len(x_plot)):
    x_char_plot.append(str(x_plot[i]))
    y_char_plot.append(str(y_plot[i]))

x_string = ''.join(x_char_plot)
y_string = ''.join(y_char_plot)

with open('q_x_new.txt', 'w') as file3:
    file3.write(x_string)

with open('q_y_new.txt', 'w') as file4:
    file4.write(y_string)

plt.plot(x_plot, y_plot)
plt.ylabel("Mean Reward Per Episode")
plt.xlabel("Episode")
plt.title("Mean Reward Per Episode vs Episode: Q_Learning")
plt.savefig("test_new.png")
