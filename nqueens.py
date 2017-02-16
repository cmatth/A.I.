# Casey Matthews
# Artificial Intelligence
# Homework 1
# NQueens Module

import numpy as np
import copy

_size  = 0
_board = 0

def newBoard(size):
	global _size
	_size  = size
	board = np.zeros(size**2)
	board = board.reshape(size,size)

	for x in range(0, _size):
		board[x][0] = 1
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
#moves the nth queen once space downward, if possible.
def move(queenNumber, board):
	thing =  np.where(board == 1)
	y = thing[1][queenNumber - 1]
	x = thing[0][queenNumber - 1]
	new = copy.deepcopy(board)

	if y < _size - 1:
		new[x][y] -= 1
		new[x][y+1] += 1
		return new
	else:
		return False

def getChildren(board):
	childs = []
	for q in range(1,_size+1):
		new = move(q,board)
		if type(new) is np.ndarray:
			childs.append(new)
	return childs
		

### TESTING ######################################################
if False:			
	board = newBoard(3)
	thing = np.where(board == 1)
	print board
	print solved(board)

	board = np.array([[0, 0, 1, 0], [1,0,0,0], [0,0,0,1], [0,1,0,0]])
	board = board.reshape(4,4)
	print board
	_size = 4
	print solved(board)
	board =  move(1, board)
	print move(1, board)
	print move(1, board)

board = np.array([[0, 0, 1, 0], [1,0,0,0], [0,0,0,1], [0,1,0,0]])
board = board.reshape(4,4)
print board
print "***********"
_size = 4
chil = getChildren(board)
for x in range(0, len(chil)):
	print chil[x]


##################################################################
