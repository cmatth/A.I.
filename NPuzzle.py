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
	for x in range(0, _size):
		print puzzle[x]

def columns(board):
	solution = True

	for y in range(0, _size):
		for x in range(0, _size - 1):
			if board[x][y] + 1 == board[x+1][y]:
				solution
			else:
				if board[x][y] == 0 or board[x+1][y] == 0:
					##### NEW ####################################
					thing =  numpy.where(board == 0)
					if thing[0] == 0 or thing[0] == _size - 1:
						solution
					else:
						if board[x][y] == 0:
							if board[x-1][y] + 1 != board[x+1][y]:
								solution = False
						else:
							if board[x][y] + 1 != board[x+2][y]:
									solution = False
					###############################################
				else:
					solution = False
					break
	if solution == True:
		return True
	else:
		solution = True
		for y in range(0, _size):
			for x in reversed(range(1, _size)):
				if board[x][y] + 1 == board[x-1][y]:
					solution
				else:
					if board[x][y] == 0 or board[x-1][y] == 0:
						##### NEW ####################################
						thing =  numpy.where(board == 0)
						if thing[0] == 0 or thing[0] == _size - 1:
							solution
						else:
							if board[x][y] == 0:
								if board[x+1][y] + 1 != board[x-1][y]:
									solution = False
							else:
								if board[x][y] + 1 != board[x-2][y]:
										solution = False
						###############################################
					else:
						solution = False
						break
	if solution == True:
		return True
	else:
		return False

def rows(board):
	solution = True

	for x in range(0, _size):
		for y in range(0, _size - 1):
			if board[x][y] + 1 == board[x][y+1]:
				solution
			else:
				if board[x][y] == 0 or board[x][y + 1] == 0:
					##### NEW ####################################
					thing =  numpy.where(board == 0)
					if thing[1] == 0 or thing[1] == _size - 1:
						solution
					else:
						if board[x][y] == 0:
							if board[x][y-1] + 1 != board[x][y+1]:
								solution = False
						else:
							if board[x][y] + 1 != board[x][y+2]:
									solution = False
					###############################################
				else:
					solution = False
					break
	if solution == True:
		return True
	else:
		solution = True
		for x in range(0, _size):
			for y in reversed(range(1, _size)):
				if board[x][y] + 1 == board[x][y - 1]:
					solution
				else:
					if board[x][y] == 0 or board[x][y - 1] == 0:
						##### NEW ####################################
						thing =  numpy.where(board == 0)
						if thing[1] == 0 or thing[1] == _size - 1:
							solution
						else:
							if board[x][y] == 0:
								if board[x][y+1] + 1 != board[x][y-1]:
									solution = False
							else:
								if board[x][y] + 1 != board[x][y-2]:
										solution = False
						###############################################
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
	if adjacency(board) == True or rows(board) == True or columns(board) == True:
	#if rows(board) == True or columns(board) == True:
	
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
	childs.append(copy.deepcopy(move("up", board)))
	childs.append(copy.deepcopy(move("down", board)))
	childs.append(copy.deepcopy(move("left", board)))
	childs.append(copy.deepcopy(move("right", board)))
	return childs

def compare(board1, board2):
	for x in range(0, _size):
		for y in range(0, _size):
			if not board1[x][y] == board2[x][y]:
				return False
	return True
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

# Testing SOLUTION VERIFIERS ##########################################################
if False:
	print "Random:"
	puzzle = newPuzzle(3)
	puzzle = puzzle.reshape(_size,_size)
	show()
	print "Rows: ", rows(puzzle)
	print "Columns: ", columns(puzzle)

	print "\nColumn forward: "
	puzzle = numpy.array([1, 4, 7, 2, 5, 8, 3, 6, 0])
	puzzle = puzzle.reshape(_size,_size)
	show()
	print "Rows: ", rows(puzzle)
	print "Columns: ", columns(puzzle)

	print "\nColumn reverse: "
	puzzle = numpy.array([0, 6, 3, 8, 5, 2, 7, 4, 1])
	puzzle = puzzle.reshape(_size,_size)
	show()
	print "Rows: ", rows(puzzle)
	print "Columns: ", columns(puzzle)

	print "\nRow forward:"
	puzzle = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
	puzzle = puzzle.reshape(_size,_size)
	show()
	print "Rows: ", rows(puzzle)
	print "Columns: ", columns(puzzle)

	print "\nRow reverse:"
	puzzle = numpy.array([0, 8, 7, 6, 5, 4, 3, 2, 1])
	puzzle = puzzle.reshape(_size,_size)
	show()
	print "Rows: ", rows(puzzle)
	print "Columns: ", columns(puzzle)
	print type(puzzle)









