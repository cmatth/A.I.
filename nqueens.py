# Casey Matthews
# Artificial Intelligence
# Homework 1
# NQueens Module

import numpy as np

_size  = 0
_board = 0

def newBoard(size):
		global _size
		_size  = size
		board = numpy.zeroes(size**2)
		board = board.reshape(size,size)

		for y in range(0, _size):
			board[0][y] = 1
		return board
end
			

