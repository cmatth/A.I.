# Casey Matthews
# Artificial Intelligence
# Homework 2
# N-Queens Hill Climbing

import numpy as np
import nqueens
import graph
import Search
import copy
import time
import operator



class State:
	def __init__(self, seed):
		self.seed  = seed
		self.board = makeState(seed)
		self.score = queensEval1(self.board)
	
	@staticmethod
	def children(self):
		best = self
		childlist = []
		better = []
		same = []
		for x in range(0,_size):
			childseed = copy.deepcopy(self.seed)
			childseed[x] = np.random.randint(0,_size,1)
			childlist.append(State(childseed))
		
		for x in childlist:
			if x.score < best.score:
				best = x
			if x.score < self.score:
				better.append(x)
			elif x.score == self.score:
				same.append(x)

		if len(better) > 0:
			randy = np.random.randint(0,len(better),1)
			return better[randy]
		elif len(same) > 0:
			randy = np.random.randint(0,len(same),1)
			return same[randy]
		else:
			return self
		
			

# returns number of conflicts in given board state
# solution should have score = 0
def queensEval1(board):

	score = 0
	firstpass = True

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

		if total2 != 0 and firstpass == False:
			score += total2 - 1

		if total3 != 0:
			score += total3 - 1

		if total4 != 0 and firstpass == False:
			score += total4 - 1

		x = np.delete(x, -1)
		y = np.delete(y, 0)
		x1 = np.delete(x1, -1)
		y1 = np.delete(y1, 0)

		firstpass = False

	#print "diagonal score: ", score

	# check sum of all rows
	
	for x in range(0, _size):
		total = 0
		for y in range(0, _size):
			total += board[x][y]

		if total != 0:
			score += total - 1

	# check sum of all columns
	
	for x in range(0, _size):
		total = 0
		for y in range(0, _size):
			total += board[y][x]

		if total != 0:
			score += total - 1
	
	#print "row score: ", score
	return score

def queensEval2(board):

	score = 0
	firstpass = True

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

		if total2 != 0 and firstpass == False:
			score += total2 - 1

		if total3 != 0:
			score += total3 - 1

		if total4 != 0 and firstpass == False:
			score += total4 - 1

		x = np.delete(x, -1)
		y = np.delete(y, 0)
		x1 = np.delete(x1, -1)
		y1 = np.delete(y1, 0)

		firstpass = False

	#print "diagonal score: ", score

	# check sum of all rows
	
	for x in range(0, _size):
		total = 0
		for y in range(0, _size):
			total += board[x][y]

		if total != 0:
			score += total - 1
	
	#print "row score: ", score
	return score

def makeState(seed):
	state = np.zeros(_size**2).reshape(_size, _size)
	
	for x in range(0,_size):
		state[seed[x], x] = 1

	return state

def replenishPop(pop):
	size = len(pop) - 2
	
	x = 0
	while x < size:
		mother = pop[x]
		father = pop[x+1]
		childs = breed(mother, father)
		for y in childs:
			pop.append(y)
		x += 2
	return pop

def breed(p1,p2):
	crossover = np.random.randint(0, _size, 1)
	childseed1 = copy.copy(p1.seed)
	childseed2 = copy.copy(p2.seed)
	for x in range(crossover, _size):
		childseed1[x] = p2.seed[x]
		childseed2[x] = p1.seed[x]

	#roll for mutation
	if np.random.randint(1, 100, 1) > 65:
		gene1 = np.random.randint(0, _size, 1)
		gene2 = np.random.randint(0, _size, 1)
		childseed1[gene1] = gene2

	#roll for mutation
	if np.random.randint(1, 100, 1) > 65:
		gene1 = np.random.randint(0, _size, 1)
		gene2 = np.random.randint(0, _size, 1)
		childseed2[gene1] = gene2


	return State(childseed1), State(childseed2)
				
		
	
	

### HILL CLIMBING #############################################################

_size = 25
_currentScore = None
seed = np.random.randint(0, _size, _size)
current = State(seed)
print current.board, current.score
restarts = 0
start = time.time()
while current.score != 0 and restarts < 30:
	next = State.children(current)
	if next != None:
		print next.board, next.score
		current = next
	else:
		restarts += 1
		print "Restarting", restarts
		current = State(np.random.randint(0, _size, _size))

if current.score == 0:
	stop = time.time()
	print "Solved:"
	print current.board
	print "Time taken: %d sec" %(stop - start)
else:
	print "Failed"





