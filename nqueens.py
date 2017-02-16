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

def solved(board):
	#check sum of all rows
	for x in range(0,_size):
		total = 0
		for y in range(0,_size):
			total += board[x][y]
			
		if total != 1 and total != 0:
			return False

	#check sum off all columns
	for y in range(0,_size):
		total = 0
		for x in range(0,_size):
			total += board[x][y]

		if total != 1 and total != 0:
			return False

	#check diagonals above main diagonal
	x = np.arange(_size)
	y = np.arange(_size)

	while len(x) > 0:
		total1 = 0
		total2 = 0
		for d in range(0,len(x)):
			total1 += board[x[d]][y[d]]
			total2 += board[y[d]][x[d]]
		
		if total1 != 1 and total1 != 0:
			return False

		if total2 != 1 and total2 != 0:
			return False

		x = np.delete(x, -1)
		y = np.delete(y, 0)

	return True
			

### TESTING ######################################################
if True:			
	board = newBoard(3)
	thing = np.where(board == 1)
	print board
	print solved(board)

	board = np.array([[0, 0, 1, 0], [1,0,0,0], [0,0,0,1], [0,1,0,0]])
	board = board.reshape(4,4)
	print board
	_size = 4
	print solved(board)
##################################################################