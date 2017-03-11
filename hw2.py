# Casey Matthews
# Artificial Intelligence
# Homework 2
# N-Queens Hill Climbing

import numpy as np
import nqueens
import graph
import Search
import copy



class State:
	def __init__(self, seed):
		self.seed  = seed
		self.board = makeState(seed)
		self.score = queensEval1(self.board)
	
	@staticmethod
	def children(self):
		childlist = []
		for x in range(0,_size):
			childseed = copy.deepcopy(self.seed)
			childseed[x] = np.random.randint(0,_size,1)
			childlist.append(State(childseed))
		
		for x in childlist:
			if x.score < self.score:
				best = x
		if best:
			return best
		
			

# returns number of conflicts in given board state
# solution should have score = 0
def queensEval1(board):

	score = 0

    # check diagonals (left to right
	x = np.arange(_size)
	y = np.arange(_size)
	x1 = x[::-1]
	y1 = y[::-1]

	while len(x) > 0:
		total1 = 0
		total2 = 0
		total3 = 0
		total4 = 0

		for d in range(0, len(x)):
			total1 += board[x[d]][y[d]]
			total2 += board[y[d]][x[d]]
			total3 += board[x1[d]][y[d]] #ASCENDING DIAGONALS BELOW MAIN
			total4 += board[y1[d]][x[d]]

		if total1 != 0:
			score += total1 - 1

		if total2 != 0:
			score += total2 - 1

		if total3 != 0:
			score += total3 - 1

		if total4 != 0:
			score += total4 - 1

		x = np.delete(x, -1)
		y = np.delete(y, 0)
		x1 = np.delete(x1, -1)
		y1 = np.delete(y1, 0)

	# check sum of all rows
	for x in range(0, _size):
		total = 0
		for y in range(0, _size):
			total += board[x][y]

			if total != 0:
				score += total - 1

	return score

def makeState(seed):
	state = np.zeros(_size**2).reshape(_size, _size)
	
	for x in range(0,_size):
		state[seed[x], x] = 1

	return state

#board = [[ 0,  0,  1,  0],[ 1,  0,  0,  0],[ 0, 0,  0,  1],[ 0,  1,  0,  0]]
#print queensEval1(board)
_size = 4
_currentScore = None
seed = np.random.randint(0, _size, _size)
start = State(seed)
print start.board, start.score
next = State.children(start)
print next.board, next.score






