# A.I. Homework Problem 1
# nxn sliding puzzle
# Casey Matthews

import numpy

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

	def solved(self):
		thing =  numpy.where(self.board == 1)
		i = int(thing[0])
		j = int(thing[1])

		for x in range(1, self.size ** 2):
			print x

	def move(direction):
		if direction == 'up': 
			#statement(s)
		elif direction == 'left': 
			#statement(s)
		elif direction == 'down': 
			#statement(s)
		else: 
			#statement(s)
		
class Test:
	def proont(self, string):
		print string

puzzle = NPuzzle(4)
puzzle.show()
puzzle.solved()


