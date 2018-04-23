# This file contains the code for the pong environment

import numpy as np
import random as rand
import math

class PongState:

    def __init__(self, ballX, ballY, vX, vY, paddle):
        self.ballX = ballX
        self.ballY = ballY
        self.vX = vX
        self.vY = vY
        self.paddle = paddle

    def setValues(self, ballX, ballY, vX, vY, paddle):
        self.ballX = ballX
        self.ballY = ballY
        self.vX = vX
        self.vY = vY
        self.paddle = paddle

    def discreteMap(self):
        bucketSize = 0.0833333333

        ballXDiscrete = math.floor(self.ballX / bucketSize)
        ballYDiscrete = math.floor(self.ballY / bucketSize)

        vXDiscrete = 0
        if(self.vX > 0):
            vXDiscrete = 1
        else:
            vXDiscrete = -1

        vYDiscrete = 0
        if(abs(self.vY) < 0.015):
            vYDiscrete = 0
        elif(self.vY > 0):
            vYDiscrete = 1
        else:
            vYDiscrete = -1

        paddleDiscrete = math.floor((12 * self.paddle) / 0.8)
        if(self.paddle == 0.8):
            paddleDiscrete = 11.0

        return (ballXDiscrete, ballYDiscrete, vXDiscrete, vYDiscrete, paddleDiscrete)

    def getState(self):
        return (self.ballX, self.ballY, self.vX, self.vY, self.paddle)

    def chooseAction(self):
        actions = [0, 0.04, -0.04]
        index = rand.randint(0,2)
        return actions[index]

    def moveNextStep(self, action_val):
        print 'MOVE BALL'
        self.ballX += self.vX
        self.ballY += self.vY

        print 'MOVE PADDLE'
        self.paddle += action_val

        U = round(rand.uniform(-0.015, 0.015), 3)
        V = round(rand.uniform(-0.03, 0.03), 3)
        if(self.ballY < 0):
            print 'TOP BOUNCE'
            self.ballY *= -1
            self.vY *= -1
        if(self.ballY > 1):
            print 'BOTTOM BOUNCE'
            self.ballY = 2 - ballY
            self.vY *= -1
        if(self.ballX < 0):
            print 'LEFT BOUNCE'
            self.ballX *= -1
            self.vX *= -1
        if(self.ballX > 1 and self.ballY > self.paddle and self.ballY < (self.paddle + .2)):
            print 'PADDLE BOUNCE'
            self.ballX = 2 - self.ballX
            self.vX = (self.vX * -1) + U
            self.vY += V

        # For every single non paddle interaction
        if self.ballX < 1:
            return 0

        # Check Miss
        if (self.ballY < self.paddle or self.ballY > self.paddle + 0.2):
            return -1

        return 1
