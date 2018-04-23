# This file will be used to test the pong agent

from pong import *
from qLearning import *
import random as rand
from tqdm import tqdm

q = qlearn()
# currState = PongState(0.5, 0.5, 0.03, 0.01, 0.4)
# currTuple = currState.getState()
# curr_key = currState.discreteMap()

for i in tqdm(range(100000)):
    ballX = round(rand.uniform(0.01, 0.99), 2)
    ballY = round(rand.uniform(0.01, 0.99), 2)
    vX = round(rand.uniform(-0.015, 0.015), 3)
    vY = round(rand.uniform(-0.03, 0.03), 3)
    paddle = round(rand.uniform(0, 0.80), 2)

    currState = PongState(ballX, ballY, vX, vY, paddle)
    currTuple = currState.getState()
    curr_key = currState.discreteMap()

    while currState.getState()[0] < 1:
        action, index = currState.chooseAction()
        # print 'Action:', action, 'Index:', index

        reward = currState.moveNextStep(action)
        next_key = currState.discreteMap()

        # print 'Reward:', reward

        # print initialState.getState()
        # print curr_key
        # print next_key

        action_q_scores = q.get_actions(next_key)

        value = reward + (0.8 * max(action_q_scores))
        # print "Value:", value

        q.set_q(curr_key, index, value)

        curr_key = next_key
        # print
