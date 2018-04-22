# This file contains the code for the pong environment

import numpy as np
import random as rand

class Pong:
    def __init__(self):
        self.ballX = 0.5
        self.ballY = 0.5
        self.velocityX = 0.03
        self.velocityY = 0.01
        self.paddleHeight = 0.2
        self.paddleY = 0.5 - (self.paddleHeight / 2)

    def getState(self):
        print "BallX:", self.ballX, "| BallY:",self.ballY, "| VelocityX:", self.velocityX, "| VelocityY:", self.velocityY, "| PaddleY:", self.paddleY

    # action -> (0 is nothing, 1 is up, 2 is down)
    def movePaddle(self, action):
        if(action == 0):
            print 'NO MOVE'
            return
        elif(action == 1):
            print 'UP MOVE'
            self.paddleY += 0.04
        else:
            print 'DOWN MOVE'
            self.paddleY -= 0.04

    def moveBall(self):
        print 'MOVE BALL'
        self.ballX += self.velocityX
        self.ballY += self.velocityY

    def bounce(self):
        U = round(rand.uniform(-0.015, 0.015), 3)
        V = round(rand.uniform(-0.03, 0.03), 3)
        if(self.ballY < 0):
            print 'TOP BOUNCE'
            self.ballY *= -1
            self.velocityY *= -1
        if(self.ballY > 1):
            print 'BOTTOM BOUNCE'
            self.ballY = 2 - ballY
            self.velocityY *= -1
        if(self.ballX < 0):
            print 'LEFT BOUNCE'
            self.ballX *= -1
            self.velocityX *= -1
        if(self.ballX > 1 and self.ballY > self.paddleY and self.ballY < (self.paddleY + self.paddleHeight)):
            print 'PADDLE BOUNCE'
            self.ballX = 2 - self.ballX
            self.velocityX += U
            self.velocityY += V
