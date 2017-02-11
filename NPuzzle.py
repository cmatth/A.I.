# A.I. Homework Problem 1
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
		thing =  numpy.where(board == 1)
		i = int(thing[0])
		j = int(thing[1])

		for x in range(1, self.size ** 2):
			print x
		return false

	def move(self, direction, board):
		# Nab the indices of the empty space
		thing =  numpy.where(board == 0)
		i = int(thing[0])
		j = int(thing[1])
		#copy the configuration
		new = copy.deepcopy(board)
		
		if direction == 'up': 
			if i > 0:
				new[i,j] = new[i-1,j]
				new[i-1,j] = 0
				return new
			else:
				return -1
		elif direction == 'left':
			if j > 0:
				new[i,j] = new[i,j-1]
				new[i,j-1] = 0
				return new
			else: 
				return -1 
		elif direction == 'down': 
			if i < self.size - 1:
				new[i,j] = new[i+1,j]
				new[i+1,j] = 0
				return new
			else: 
				return -1
		elif direction == 'right':
			if j < self.size - 1:
				new[i,j] = new[i,j+1]
				new[i,j+1] = 0
				return
			else: 
				return -1 
		else:
				return -1
		
class Test:
	def proont(self, string):
		print string

puzzle = NPuzzle(4)
puzzle.show()
print "\n", puzzle.move('up', puzzle.board), "\n"
print puzzle.move('down', puzzle.board), "\n"
print puzzle.move('right', puzzle.board), "\n"
print puzzle.move('left', puzzle.board)



