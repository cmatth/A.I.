# A.I. Homework Problem 
# nxn sliding puzzle
# Casey Matthews

import numpy
import copy


puzzle = 0
_size  = 0

def newPuzzle(size):
	board  = numpy.arange(size*size)
	numpy.random.shuffle(board)
	board  = board.reshape(size,size)
	global _size 
	global   puzzle
	_size  = size
	puzzle = board
	return   board

# May no longer need reset()
def reset():
	puzzle = puzzle.reshape(_size ** 2)
	numpy.random.shuffle(puzzle)
	puzzle = puzzle.reshape(_size, _size)

def show():
	print puzzle

def columns(board):
	solution = True

	for y in range(0, _size - 1):
		for x in range(0, _size - 2):
			if board[x][y] == board[x+1][y]:
				solution = True
			else:
				if board[x][y] == 0 or board[x-1][y] == 0:
					solution = True
				else:
					solution = False
					break
	if solution == True:
		return True
	else:
		solution = True
		for y in range(0, _size - 2):
			for x in range(_size - 1, 1):
				if board[x][y] == board[x-1][y]:
					solution = True
				else:
					if board[x][y] == 0 or board[x-1][y] == 0:
						solution = True
					else:
						solution = False
						break
	if solution == True:
		return True
	else:
		return False

def rows(board):
	solution = True

	for y in range(0, _size - 2):
		for x in range(0, _size - 1):
			if board[y][x] == board[y+1][x]:
				solution = True
			else:
				if board[x][y] == 0 or board[x-1][y] == 0:
					solution = True
				else:
					solution = False
					break
	if solution == True:
		return True
	else:
		solution = True
		for y in range(0, _size - 2):
			for x in range(_size - 1, 1):
				if board[y][x] == board[y-1][x]:
					solution = True
				else:
					if board[x][y] == 0 or board[x-1][y] == 0:
						solution = True
					else:
						solution = False
						break
	if solution == True:
		return True
	else:
		return False		

def adjacency(board):
	#Starting from the tile containing 1
	thing =  numpy.where(board == 1)
	indexLimit = _size - 1
	i = int(thing[0])
	j = int(thing[1])
		
	#Look in all adjacent spaces to find the
	#next sequential tile
	for x in range(2, _size ** 2):
		left  = 'E'
		right = 'E'
		above = 'E'
		below = 'E'

		if i < indexLimit: #can check left of focus
			below = board[i+1][j]
		if i > 0:
			above = board[i-1][j]
		if j > 0:
			left  = board[i][j-1]
		if j < indexLimit:
			right = board[i][j+1]

		if   x == above:
			i -= 1
		elif x == below:
			i += 1
		elif x == right:
			j += 1
		elif x == left:
			j -= 1
		else:
			return False
	return True

def solved(board):
	print "verifier"
	if adjacency(board) == True or rows(board) == True or columns(board) == True:
		return True
	else:
		return False
	
	# Moves the empty space in the indicated direction(if it can), then
	# returns the new board state. Returns -1 on unsuccessful move
def move(direction, board):
	# Nab the indices of the empty space
	thing =  numpy.where(board == 0)
	i = int(thing[0])
	j = int(thing[1])
	#copy the configuration
	new = copy.deepcopy(board)
		
	if direction == 'up': 
		if up(i):
			new[i,j] = new[i-1,j]
			new[i-1,j] = 0
			return new
		else:
			return -1
	elif direction == 'left':
		if left(j):
			new[i,j] = new[i,j-1]
			new[i,j-1] = 0
			return new
		else: 
			return -1 
	elif direction == 'down': 
		if down(i):
			new[i,j] = new[i+1,j]
			new[i+1,j] = 0
			return new
		else: 
			return -1
	elif direction == 'right':
		if right(j):
			new[i,j] = new[i,j+1]
			new[i,j+1] = 0
			return new
		else: 
			return -1 
	else:
		return -1

	# These methods verify that requested move is a legal one
def up(i):
	if i > 0:
		return True
	else:
		return False
			
def down(i):
	if i < _size - 1:
		return True
	else:
		return False

def left(j):
	if j > 0:
		return True
	else:
		return False

def right(j):
	if j < _size - 1:
		return True
	else:
		return False

def children(board):
	childs = []
	childs.append(move("up", board))
	childs.append(move("down", board))
	childs.append(move("left", board))
	childs.append(move("right", board))
	return childs
		
	#########################################################
			
		
# TESTING MOVEMENT #######################################################################
if False:
	puzzle = newPuzzle(18)
	print "Orignal Board:"
	show()
	print "UP:"
	print move('up', puzzle)
	print "DOWN:"
	print move('down', puzzle)
	print "RIGHT:"
	print move('right', puzzle)
	print "LEFT:"
	print move('left', puzzle)
#########################################################################################

# TESTING SOLUTIONS #####################################################################
if False:
	size = 4
	puzzle = numpy.arange(size*size)
	puzzle = puzzle.reshape(size,size)
	print puzzle
	puz = NPuzzle(4)
	print puz.solved(puzzle)

	puz = NPuzzle(3)
	size = 3
	puzzle = numpy.array([1, 4, 7, 2, 5, 8, 3, 6, 0])
	puzzle = puzzle.reshape(size,size)
	print puzzle
	print puz.solved(puzzle)
##########################################################################################

# Testing new puzzle style code ##########################################################
if False:
	puzzle = newPuzzle(3)
	show()
	puzzle = numpy.array([1, 4, 7, 2, 5, 8, 3, 6, 0])
	puzzle = puzzle.reshape(_size,_size)
	print solved(puzzle)









