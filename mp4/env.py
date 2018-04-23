# This file will be used to test the pong agent

from pong import *

initialState = PongState(0.99, 0.5, 0.03, 0.01, 0.4)
initialTuple = initialState.getState()
initialDTuple = initialState.discreteMap()
print initialTuple
print initialDTuple

# rewards = []
# for idx in range(12):
#     temp = (11, idx)
#     rewards.append(temp)

action = initialState.chooseAction()
print action

reward = initialState.moveNextStep(action)
print initialState.getState(), initialState.discreteMap()
print reward
