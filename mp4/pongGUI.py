from pong import *
from qLearning import *
import json
import os
import numpy as np
import random as rand
import math
import pygame, sys
from pygame.locals import *

# Letting Max FPS be 1000
FramesPerSecond = 200
SPEED = 1

# WindowWidth and WindowHeight
WW = 800
WH = 400

#LineThickness, PaddleSize, Paddleoffset
LT = 10
PS = 80
POF = 20

#Colors BLACK and White
BL = (0,0,0)
WHT = (255,255,255)

def arena():
    DISP.fill((0,0,0))
    pygame.draw.rect(DISP, WHT, ((0,0),(WW, WH)), LT*2)
    pygame.draw.line(DISP, WHT, (WW/2 , 0), (WW/2 , WH), LT/4)

def paddle(pad):
    if pad.bottom > WH-LT:
        pad.bottom = WH - LT
    elif pad.top < LT:
        pad.top = LT

    pygame.draw.rect(DISP, WHT, pad)

def ball(bl):
    pygame.draw.rect(DISP, WHT, bl)

def mBl(bl, blPOSX, blPOSY):
    bl.x += (blPOSX*SPEED)
    bl.y += (blPOSY*SPEED)
    return bl

def checkColl(bl, blPOSX, blPOSY):
    if bl.top == LT or bl.bottom == (WH-LT) :
        blPOSY = blPOSY * -1
    if bl.left == LT or bl.right == (WW-LT) :
        blPOSX = blPOSX * -1
    return blPOSX, blPOSY

def checkCollBl(bl, pad1, pad2, blPOSX):
    U = int((round(rand.uniform(-0.015, 0.015), 3)) * SPEED)
    V = int((round(rand.uniform(-0.03, 0.03),3)) * SPEED)
    U = 0
    V = 0
    if blPOSX == -1 and pad1.right == bl.left and pad1.top < bl.top and pad1.bottom > bl.bottom:
            return -1, U, V
    elif blPOSX == 1 and pad2.left == bl.right and pad2.top < bl.top and pad2.bottom > bl.bottom:
        return -1, U, V
    else:
        return 1, 0, 0

def AI(bl, pad2, blPOSX, blPOSY, q):
    if bl.x > (WW - POF -LT) or bl.x < WW/2 :
        return pad2
    else:
        blXDiscrete = int(math.floor(((bl.centerx-(WW/2))/(WW/2))*12))
        blYDiscrete = int(math.floor((bl.centery/WH)*12))
        padxDiscrete = int(math.floor((12*(pad2.centery/WH))/(1-(PS/WH))))
        currentState = (blXDiscrete, blYDiscrete, blPOSX, blPOSY, padxDiscrete)
        paddle_actions = [0, 0.04, -0.04]
        action_idx = np.argmax(q.get_actions(currentState))
        action = paddle_actions[action_idx]
        if action > 0:
            pad2.y += SPEED
        elif action < 0:
            pad2.y -= SPEED
        return pad2

def main():
    pygame.init()
    global DISP

    FSClock = pygame.time.Clock()
    DISP = pygame.display.set_mode((WW,WH))
    pygame.display.set_caption('PONG GUI')

    blX = WW/2 - LT/2
    blY = WH/2 - LT/2
    p1POS = (WH-PS)/2
    p2POS = (WH-PS)/2

    blPOSX = -1
    blPOSY = -1

    pad1 = pygame.Rect(POF, p1POS, LT, PS)
    pad2 = pygame.Rect(WW - POF - LT, p2POS, LT, PS)
    bl = pygame.Rect(blX, blY, LT, LT)

    arena()
    paddle(pad1)
    paddle(pad2)
    ball(bl)

    pygame.mouse.set_visible(0)

    q = qlearn()
    current_path = os.getcwd()
    path1 = "/qmat_old.txt"
    path2 = "/string_object_map_old.txt"

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

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == MOUSEMOTION:
                mx, my = e.pos
                pad1.y = my

        arena()
        paddle(pad1)
        paddle(pad2)
        ball(bl)

        bl = mBl(bl, blPOSX, blPOSY)
        blPOSX, blPOSY = checkColl(bl, blPOSX, blPOSY)
        dir, U, V =  checkCollBl(bl, pad1, pad2,blPOSX)
        blPOSX = (blPOSX*dir) + U
        blPOSY = blPOSY + V
        pad2 = AI(bl, pad2, blPOSX, blPOSY, q)


        pygame.display.update()
        FSClock.tick(FramesPerSecond)

if __name__=='__main__':
    main()
