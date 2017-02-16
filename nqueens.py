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
		board = np.zeros(size**2)
		board = board.reshape(size,size)

		for y in range(0, _size):
			board[0][y] = 1
		return board
			
board = newBoard(3)
thing = np.where(board == 1)
print thing[1][2], 

def solved(board)
		thing = np.where(board == 1)
		for y in range(0, len(thing[0]))
			queens = 
