# This file will be used to test the pong agent

from pong import *
from qLearning import *

q = qlearn()
initialState = PongState(0.99, 0.5, 0.03, 0.01, 0.4)
initialTuple = initialState.getState()
initialDTuple = initialState.discreteMap()
curr_key = initialDTuple

print initialDTuple

# rewards = []
# for idx in range(12):
#     temp = (11, idx)
#     rewards.append(temp)

action, index = initialState.chooseAction()
print action, index

reward = initialState.moveNextStep(action)
next_key = initialState.discreteMap()

print reward

print initialState.getState()
print next_key

action_q_scores = q.get_actions(next_key)

value = reward + max(action_q_scores)
print "Value:", value

q.set_q(curr_key, index, value)
