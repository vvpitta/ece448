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
                ##Find if connect 5 window can exist on diagonal if so then traverse diagonal
                ##posxintercept = int((1*(i)) + j)
                                
     
	
	def upateBoard(self, i, j, ply):
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
			
##class MinMax:
		
	def evaluate(game, ply):
              	'''if game.ko == True and winner == ply:
                       return 
                elif game.ko == True:
                       return -1*math.inf 
                else:'''
        	return (game.count[ply][0] * 1) + (game.count[ply][1] * 2)  + (game.count[ply][2] * 3) + (game.count[ply][3] * 4) 
                                        
	def miniMax(game, move, ply):
                if move == 0 and ply == 0
                        return 3,3 
                else:
                        move = getNextMove(0, game, True, False, ply, -1, -1)
                        return move[0], move[1]
                        
	def isValid(x, y, game):
		if game.board[x][y] == '.':
			return True
		return False
	
	expandedNodesMinMax = 0
	
	def getNextMove(depth, game, agent, ply, x, y):
                if game.ko == True and agent:
                        return [x,y,1000000000000]
                elif game.ko == True : 
                        return [x,y,-1000000000000]
		if depth == 3:
			return [x,y,evaluate(game, ply)]
                ## keeping track of the best move so far for the agent and the opposition
		expandedNodesMinMax = expandedNodesMinMax + 1 ##Does this make sense for expanded nodes, because each time we recurse through we expand a node
		choicesAgent = [-1,-1,-1000000000000] ## x,y (move), value of move
		choicesOpp = [-1,-1,1000000000000]
		if agent:
			for i in range(7):
				for j in range(7):
					gamecopy = Gomuku()
					gamecopy.copycat(game)
					if isValid(i,j, gamecopy):
						gamecopy.upateBoard(i,j, ply)
						if ply == 0
							maxmoves = getNextMove(depth+1, gamecopy, False, 1, i, j)
						else:
							maxmoves = getNextMove(depth+1, gamecopy, False, 0, i, j)
						if maxmoves[2] > choicesAgent[2]:
							choicesAgent[0] = i
							choicesAgent[1] = j
		else:
			for i in range(7):
				for j in range(7):
					gamecopy = game
					if isValid(i,j, gamecopy):
						gamecopy.upateBoard(i,j, agent, ply)
						if ply == 0
							minmoves = getNextMove(depth+1, gamecopy, True, 1, i, j)
						else:
							minmoves = getNextMove(depth+1, gamecopy, True, 0, i, j)
						if minmoves[2] < choicesOpp[2]:
							choicesOpp[0] = i
							choicesOpp[1] = j
		## it should only reach this return statement after the evaluation of the entire tree
		return choicesAgent
		
			
	def alphaBeta(game, move, ply):
                if move == 0 and ply == 0
                        return 3,3
                else:
			alpha = [-1,-1,1000000000000]
			beta = [-1,-1,-1000000000000]
                        getNextMoveAlphaBeta (0, game, True, ply, -1000000000000, +1000000000000, -1, -1)

	expandedNodesAlphaBeta = 0
        def getNextMoveAlphaBeta (depth, game, agent, ply, alpha, beta, x, y)  ## alpha [-1,-1, -inf] and beta [-1,-1, +inf]
                if game.ko == True and agent == True : 
                        return [x,y,1000000000000]##math.inf +ve inf
                elif game.ko == True:
                        return [x,y,-1000000000000]##-ve inf   -1*float(math. 
		if depth == 3:
			return [x,y,evaluate(game, ply)]
                expandedNodesAlphaBeta = expandedNodesAlphaBeta + 1
		if agent:
			best = [-1,-1,-1000000000000] ##(-100,000,000,000)
                        for i in range(7):
				doublebreak = False
                                for j in range(7):
                                        gamecopy = Gomuku()
                                        gamecopy.copycat(game)
                                        if isValid(i,j, gamecopy):
                                              gamecopy.updateBoard(i,j, ply)
					      if ply == 0:
                                              	value = getNextMoveAlphaBeta(depth+1, gamecopy, False, 1, alpha, beta i, j)
					      else:
	                       			value = getNextMoveAlphaBeta(depth+1, gamecopy, False, 0, alpha, beta i, j)
					if value[2] >= best[2]:
					     best = value
					if best[2] >= alpha[2]:
					      alpha = best
					if beta[2] <= alpha[2]:
					      doublebreak = True
					      break
				if doublebreak:
					      break
			return best
		else:
			best = [-1,-1,1000000000000] ##(-100,000,000,000)
                	for i in range(7):
				doublebreak = False
                                for j in range(7):
                                        gamecopy = Gomuku()
                                        gamecopy.copycat(game)
                                        if isValid(i,j, gamecopy):
                                              gamecopy.updateBoard(i,j, ply)
					      if ply == 0:
                                              	value = getNextMoveAlphaBeta(depth+1, gamecopy, True, 1, alpha, beta, i, j)
					      else:
	                       			value = getNextMoveAlphaBeta(depth+1, gamecopy, True, 0, alpha, beta, i, j)
					if value[2] <= best[2]:
					     best = value
					if best[2] <= alpha[2]:
					      alpha = best
					if beta[2] <= alpha[2]:
					      doublebreak = True
					      break
				if doublebreak:
					      break
			return best
					      
	def playGame()
					 
					      
					      
					      

                                              
                                              
                                                                                                            
                                                            
                                        
