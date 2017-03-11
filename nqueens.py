# Casey Matthews
# Artificial Intelligence
# Homework 1
# NQueens Module

import numpy as np
import copy
import math

_size = 0
_board = 0


def newBoard(size):
    global _size
    _size = size
    board = np.zeros(size ** 2)
    board = board.reshape(size, size)

    for x in range(0, _size):
        board[x][0] = 1
    return board


def solved(board):
    # check sum of all rows
    for x in range(0, _size):
        total = 0
        for y in range(0, _size):
            total += board[x][y]

        if total != 1 and total != 0:
            return False

    # check sum off all columns
    for y in range(0, _size):
        total = 0
        for x in range(0, _size):
            total += board[x][y]

        if total != 1 and total != 0:
            return False

    # check diagonals (left to right
    x = np.arange(_size)
    y = np.arange(_size)
    y1 = y[::-1]

    while len(x) > 0:
        total1 = 0
        total2 = 0
        total3 = 0
        total4 = 0
        for d in range(0, len(x)):
            total1 += board[x[d]][y[d]]
            total2 += board[y[d]][x[d]]
            total3 += board[x[d]][y1[d]]
            total4 += board[y1[d]][x[d]]

        if total1 != 1 and total1 != 0:
            return False

        if total2 != 1 and total2 != 0:
            return False

        if total3 != 1 and total3 != 0:
            return False

        if total4 != 1 and total4 != 0:
            return False

        x = np.delete(x, -1)
        y = np.delete(y, 0)
        y1 = np.delete(y1, 0)
    return True


def directMove(queenNumber, board, direct):
    if direct == 1:
        return move(queenNumber, board)
    else:
        return moveBack(queenNumber, board)


# moves the nth queen once space downward, if possible.
def move(queenNumber, board):
    thing = np.where(board == 1)
    y = thing[1][queenNumber - 1]
    x = thing[0][queenNumber - 1]
    new = copy.deepcopy(board)

    if y < _size - 1:
        new[x][y] -= 1
        new[x][y + 1] += 1
        return new
    else:
        return False


def moveBack(queenNumber, board):
    thing = np.where(board == 1)
    y = thing[1][queenNumber - 1]
    x = thing[0][queenNumber - 1]
    new = copy.deepcopy(board)

    if y > 0:
        new[x][y] -= 1
        new[x][y - 1] += 1
        return new
    else:
        return False


def getChildren(board):
    childs = []
    for q in range(1, _size + 1):
        new = move(q, board)
        if type(new) is np.ndarray:
            childs.append(new)
    return childs


def getChildrenD(board, direct):
    childs = []
    for q in range(1, _size + 1):
        new = directMove(q, board, direct)
        if type(new) is np.ndarray:
            childs.append(new)
    return childs


def spaceSize():
    return float(_size ** _size) * .01


def goalState():
    if _size == 5:
        return np.array([[0., 1., 0., 0., 0.],
                         [0., 0., 0., 1., 0.],
                         [1., 0., 0., 0., 0.],
                         [0., 0., 1., 0., 0.],
                         [0., 0., 0., 0., 1.]])

    if _size == 4:
        return np.array([[0., 1., 0., 0.],
                         [0., 0., 0., 1.],
                         [1., 0., 0., 0.],
                         [0., 0., 1., 0.]])

#### New implementation ##################################
def getInitialState(size):
    global _size
    _size = size
    return np.zeros(_size ** 2).reshape(size, size)

def childrens(config):
    #Sum all elements to determine queen number
    j = np.arange(0, _size)
    sum = 0
    childs = []
    for x in range(0, _size):
            for y in range(0, _size):
                if config[x][y] == 1:
                    sum += 1
                    index = np.argwhere(j == y)
                    j = np.delete(j,index)
    if len(j) != 0 and sum < _size:
        for c in j:
            new = copy.deepcopy(config)
            new[sum][c] += 1
            childs.append(new)
    else:
        return []
    return childs

def solvedNew(board):
    #check that all queens are placed
    sum = 0
    for x in range(0, _size):
        for y in range(0, _size):
            if board[x][y] == 1:
                sum += 1
    if sum < _size:
       # print "imcomplete solution"
        return False

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
        #print "::::::::::::"
        for d in range(0, len(x)):
            total1 += board[x[d]][y[d]]
            total2 += board[y[d]][x[d]]
            total3 += board[x1[d]][y[d]] #ASCENDING DIAGONALS BELOW MAIN
            total4 += board[y1[d]][x[d]]
          #  print y1[d], x1[d], x1[d], y[d]
        if total1 != 1 and total1 != 0:
            return False

        if total2 != 1 and total2 != 0:
            return False

        if total3 != 1 and total3 != 0:
            return False

        if total4 != 1 and total4 != 0:
            return False

        x = np.delete(x, -1)
        y = np.delete(y, 0)
        x1 = np.delete(x1, -1)
        y1 = np.delete(y1, 0)
    return True

def spaceSizeNew():
    return float(math.factorial(_size)) * .02673
### TESTING ######################################################
if False:
    board = newBoard(3)
    thing = np.where(board == 1)
    print board
    print solved(board)

    board = np.array([[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]])
    board = board.reshape(4, 4)
    print board
    _size = 4
    print solved(board)
    board = move(1, board)
    print move(1, board)
    print move(1, board)

if False:
    board = np.array([[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]])
    board = board.reshape(4, 4)
    print board
    print "***********"
    _size = 4
    chil = getChildren(board)
    for x in range(0, len(chil)):
        print chil[x]

if False:
    _size = 7

    '''
    puzzle = [[ 0.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0.],
              [ 0.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0.],
              [ 0.  ,0.  ,0.  ,0.  ,1.  ,1.  ,0.  ,0.],
              [ 0.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0.  ,1.],
              [ 0.  ,0.  ,1.  ,0.  ,0.  ,0.  ,0.  ,0.],
              [ 0.  ,0.  ,0.  ,0.  ,1.  ,0.  ,0.  ,0.],
              [ 0.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0.],
              [ 0.  ,1.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0.]]
    '''
    puzzle = [[ 0.,  0.,  0.,  0.,  0.,  0.,  1.,],
              [ 0.,  0.,  0.,  0.,  1.,  0.,  0.],
              [ 0.,  0.,  0.,  1.,  0.,  0.,  0.],
              [ 0.,  0.,  1.,  0.,  0.,  0.,  0.],
              [ 1.,  0.,  0.,  0.,  0.,  0.,  0.],
              [ 0.,  0.,  0.,  0.,  0.,  1.,  0.],
              [ 0.,  1.,  0.,  0.,  0.,  0.,  0.]]

    print solvedNew(puzzle)



##################################################################
