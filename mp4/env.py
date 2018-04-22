# This file will be used to test the pong game

from pong import *

game = Pong()
game.getState()

game.movePaddle(0)
game.getState()

game.moveBall()
game.getState()

game.bounce()
game.getState()
