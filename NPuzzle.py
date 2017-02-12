# A.I. Homework Problem 
# nxn sliding puzzle
# Casey Matthews

import numpy
import copy

class NPuzzle:
	def __init__(self, size):
		self.newPuzzle(size)
		self.size = size

	def newPuzzle(self, size):
		board = numpy.arange(size*size)
		numpy.random.shuffle(board)
		board = board.reshape(size,size)
		self.board =  board
		self.size  =  size

	def reset(self):
		board = self.board.reshape(self.size*self.size)
		numpy.random.shuffle(board)
		self.board = board.reshape(self.size, self.size)

	def show(self):
		print self.board

	def solved(self, board):
		#Starting from the tile containing 1
		thing =  numpy.where(board == 1)
		i = int(thing[0])
		j = int(thing[1])

		#print "%s @ (%s,%s)" %(board[i,j], i, j)
		
		#Look in all adjacent spaces to find the
		#next sequential tile
		for x in range(2, self.size ** 2):
			'''
			if   self.left() x == board[ i     ][ j - 1 ]:
				j -= 1
			elif x == board[ i - 1 ][ j     ]:
				i -= 1
			elif x == board[ i + 1 ][ j     ]:
				i += 1
			elif x == board[ i     ][ j + 1 ]:
				j += 1
			else:
				return False
			''' 		
		return True
	
	# Moves the empty space in the indicated direction(if it can), then
	# returns the new board state. Returns -1 on unsuccessful move
	def move(self, direction, board):
		# Nab the indices of the empty space
		thing =  numpy.where(board == 0)
		i = int(thing[0])
		j = int(thing[1])
		#copy the configuration
		new = copy.deepcopy(board)
		
		if direction == 'up': 
			if self.up(i):
				new[i,j] = new[i-1,j]
				new[i-1,j] = 0
				return new
			else:
				return -1
		elif direction == 'left':
			if self.left(j):
				new[i,j] = new[i,j-1]
				new[i,j-1] = 0
				return new
			else: 
				return -1 
		elif direction == 'down': 
			if self.down(i):
				new[i,j] = new[i+1,j]
				new[i+1,j] = 0
				return new
			else: 
				return -1
		elif direction == 'right':
			if self.right(j):
				new[i,j] = new[i,j+1]
				new[i,j+1] = 0
				return new
			else: 
				return -1 
		else:
				return -1

	# These methods verify that requested move is a legal one
	def up(self, i):
		if i > 0:
			return True
		else:
			return False
			
	def down(self, i):
		if i < self.size - 1:
			return True
		else:
			return False

	def left(self, j):
		if j > 0:
			return True
		else:
			return False

	def right(self, j):
		if j < self.size - 1:
			return True
		else:
			return False
	#########################################################
			
		
# TESTING MOVEMENT #######################################################################
if True:
	puzzle = NPuzzle(4)
	print "Orignal Board:"
	puzzle.show()
	print "UP:"
	print puzzle.move('up', puzzle.board)
	print "DOWN:"
	print puzzle.move('down', puzzle.board)
	print "RIGHT:"
	print puzzle.move('right', puzzle.board)
	print "LEFT:"
	print puzzle.move('left', puzzle.board)
#########################################################################################

# TESTING SOLUTIONS #####################################################################
if False:
	size = 4
	puzzle = numpy.arange(size*size)
	puzzle = puzzle.reshape(size,size)
	print puzzle
	puz = NPuzzle(4)
	print puz.solved(puzzle)


