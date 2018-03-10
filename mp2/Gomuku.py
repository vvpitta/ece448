import collections
import util
import copy

class Gomuku:

	def _init__(self):
		self.board = [['.' for i in range(7)] for i in range(7)]
		##self.np = 1
		##slef.lm = (-1, -1)
		self.pOne = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
		self.pTwo = ['A','B','C','D','E'.'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
		##self.steps = [0,0]
		self.count = [[0 for i in range(4)] for j in range(2)]
                self.ko = False
                self.winner = -1
	##override = functions 
        ##final 
	##if 1st move then place in middle

        def copycat(self, game):
                self.board = copy.deepcopy(game.board)
                self.pOne = copy.deepcopy(game.pOne)
                self.pTwo = copy.deepcopy(game.pTwo)
                ##self.steps = copy.deepcopy(game.steps)
                self.ko = copy.deepcopy(game.ko)
                self.winner = copy.deepcopy(game.winner)
                
	def winCount(self, i,j):
		for x in range(3):
			wcount = 0
			pcount = 0
			for b in range(5):
                                check = x + b
                                if board.[check][j].islower():
                                        wcount = wcount + 1
                                elif board.[check][j].isupper():
                                        wcount = -1
                                        pcount = pcount + 1
                        if wcount == 5:
                                self.ko = True
                                self.winner = 0
                                return
                        if pcount == 5:
                                self.ko = True
                                self.winner = 1
                                return
                        if wcount > 0:
				self.count[0][wcount-1] = self.count[0][wcount-1] + 1
				if wcount == 4:
                                        self.count[0][2] = self.count[0][2] - 1
                                if wcount == 3:
                                        self.count[0][1] = self.count[0][1] - 1
                                if wcount == 2:
                                        self.count[0][0] = self.count[0][0] - 1
			if pcount > 0:
                                self.count[1][pcount-1] = self.count[ply+1][pcount-1] + 1
                                if pcount == 4:
                                        self.count[0][2] = self.count[0][2] - 1
                                if pcount == 3:
                                        self.count[0][1] = self.count[0][1] - 1
                                if pcount == 2:
                                        self.count[0][0] = self.count[0][0] - 1
     
		for y in range(3):
			wcount = 0
			pcount = 0
			for b in range(5):
                                check = y + b
                                if board.[i][check].islower():
                                        wcount = wcount + 1
                                        pcount = -1
                                elif board.[check][j].isupper():
                                        wcount = -1
                                        pcount = pcount + 1
                         if wcount == 5:
                                self.ko = True
                                self.winner = 0
                                return
                        if pcount == 5:
                                self.ko = True
                                self.winner = 1
                                return
			if wcount > 0:
				self.count[0][wcount-1] = self.count[0][wcount-1] + 1
				if wcount == 4:
                                        self.count[0][2] = self.count[0][2] - 1
                                if wcount == 3:
                                        self.count[0][1] = self.count[0][1] - 1
                                if wcount == 2:
                                        self.count[0][0] = self.count[0][0] - 1
			if pcount > 0:
                                self.count[1][pcount-1] = self.count[ply+1][pcount-1] + 1
                                if pcount == 4:
                                        self.count[0][2] = self.count[0][2] - 1
                                if pcount == 3:
                                        self.count[0][1] = self.count[0][1] - 1
                                if pcount == 2:
                                        self.count[0][0] = self.count[0][0] - 1
                
                
                ##to find diagonal
                ##Use slope = 1 and slope = -1 to determine points, rely on isoceles triangle rule
                ## Find if connect 5 can exist on diagonal if so then traverse diagonal
                
                posxintercept = int((1*(i)) + j)
                                
     
	
	def upateBoard(i,j, ply):
		if ply = 0 and self.board[i][j] == '.':
			self.board[i][j] = self.pOne[0]
			self.pOne.pop(0)
			##self.steps[0] = self.steps[0] + 1
                        self.winCount(i,j)
					
		elif ply = 2 and self.board[i][j] == '.':
			self.board[i][j] = self.pTwo[0]
			self.pTwo.pop(0)
			##self.steps[1] = self.steps[1] + 1
                        self.winCount(i,j)
			
		



		
##class MinMax{
		
	def evaluate(game, ply):
                  if game.ko == True and winner == ply:
                       return 
                elif game.ko == True:
                       return -1*math.inf
                else:
                        return (game.count[ply][0] * 1) + (game.count[ply][1] * 2)  + (game.count[ply][2] * 3) + (game.count[ply][3] * 4) 
                                        
	def miniMax(game, move, ply):
                if move == 0 and ply == 0
                        return 3,3
                        
                else:
                        move = getNextMove(0, game, True, False, ply)
                        return move[0], move[1]
                        
	
	def isValid(x, y, game):
		if game.board[x][y] == '.':
			return True
		return False
		
	def getNextMove(depth, game, agent, opp, ply):
		##gamecopy = game
		##if game is over return -inf or +inf based on if agent or opp --> do I need to do this
                if game.ko = True and game.winner = ply
                        return ##math.inf +ve inf
                elif game.ko = True
                        return ##-ve inf   -1*float(math. 
		if depth == 3:
			return evaluate(game, ply)
                choicesAgent = [0,0,-math.inf] ## x,y (move), value of move
		choicesOpp = [0,0,math.inf]
		if agent:
			for i in range(7):
				for j in range(7):
					gamecopy = Gomuku()
					gamecopy.copycat(game)
					if isValid(i,j, gamecopy):
						gamecopy.upateBoard(i,j,agent, opp)
						maxmoves = (getNextMove(depth+1, gamecopy, False, True)
						if maxmoves > choicesAgent[2]:
							choicesAgent[0] = i
							choicesAgent[1] = j
		if opp:
			for i in range(7):
				for j in range(7):
					gamecopy = game
					if isValid(i,j, gamecopy):
						gamecopy.upateBoard(i,j, agent, opp)
						minmoves = getNextMove(depth+1, gamecopy, True, False)
						if minmoves < choicesOpp[2]:
							choicesOpp[0] = i
							choicesOpp[1] = j
		return choicesAgent
		
			
	def alphaBeta(game, move, ply):
                if move == 0 and ply == 0
                        return 3,3
                else:
                        getNextMoveAlphaBeta (0, game, True, ply, ##-infinity, +infinity)


        def getNextMoveAlphaBeta (depth, value, game, agent, opp, ply, alpha, beta)
                if game.ko = True and game.winner = ply
                        return ##math.inf +ve inf
                elif game.ko = True
                        return ##-ve inf   -1*float(math. 
		if depth == 3:
			return evaluate(game, ply)
                
                if agent:
                        for i in range(7):
                                for j in range(7):
                                        gamecopy = Gomuku()
                                        gamecopy.copycat(game)
                                        if isValid(i,j, gamecopy):
                                              gamecopy.updateboard(i,j, agent, opp)
                                              value = 
                                              
                                              
                                                                                                            
                                                            
                                        
