# Casey Matthews
# Artificial Intelligence Spring 2017
# Search Algorithms

import numpy as np
import Queue
import NPuzzle as p
import math

#Module Vars
space = 0

def GraphSearch(config, verify, makeChildren, searchAlgorithm):
	return searchAlgorithm(config, verify, makeChildren)

def BreadthFirst(root, verifier, children):
	Open = [] 
	solutions = []
	Open.append(root)
	closed   = []
	solution = False
	visited = False
	count = 0 #for progress
	global space
	space = float(math.factorial(p._size ** 2))

	while not len(Open) == 0:
		state = Open[0]
		Open.remove(state)
		solution = verifier(state)

		#Progress
		count += 1
		#Progress(count)
		
		if solution == False:
			closed.append(state)
			newChil = children(state)
	
			for x in newChil:
				if type(x) is np.ndarray:
					visited = False
					print "before"
					for o in Open:
						if p.compare(x, o):
							visited = True
							break
					if visited == False:
						for c in closed:
							if p.compare(x, c):
								visited = True
								break
					if visited == False:
						Open.append(x)
					print "after"
		else:
			return [True, state]
	return [False, 'could not find solution']

def BreadthFirstT(root, verifier, children):
	Open = []
	closed   = set([]) 
	solutions = []
	Open.append(convertBoard(root))
	solution = False
	visited = False
	count = 0 #for progress
	global space
	space = float(math.factorial(p._size ** 2))

	while not len(Open) == 0:
		#get matrix and tuple representations from Open
		#then remove from open
		state = convertTuple(Open[0])
		record = Open[0]
		Open.remove(record)

		#Check if state is a solution
		solution = verifier(state)

		#Progress
		count += 1
		Progress(len(closed))
		
		
		if solution == False:
			closed.add(record)
			newChil = children(state)
	
			#check if any new children are repeated states
			for x in newChil:
				if type(x) is np.ndarray:
					x = convertBoard(x)
					if x not in closed:
						if x not in Open:
							Open.append(x)	

		else:
			return [True, state]
	return [False, "could not find solution"]

def DepthFirstT(root, verifier, children):
	Open = []
	closed   = set([]) 
	solutions = []
	Open.append(convertBoard(root))
	solution = False
	visited = False
	count = 0 #for progress
	global space
	space = float(math.factorial(p._size ** 2))

	while not len(Open) == 0:
		#get matrix and tuple representations from Open
		#then remove from open
		record = Open.pop()
		state = convertTuple(record)
		Open.remove(record)

		#Check if state is a solution
		solution = verifier(state)

		#Progress
		count += 1
		Progress(len(closed))
		
		
		if solution == False:
			closed.add(record)
			newChil = children(state)
	
			#check if any new children are repeated states
			for x in newChil:
				if type(x) is np.ndarray:
					x = convertBoard(x)
					if x not in closed:
						if x not in Open:
							Open.append(x)		
		else:
			solutions.append(state)
	return solutions							
			
def Progress(count):
	progress = (count / space) * 202
	print 'Space Traversed [%d%%]\r'%progress,

def convertBoard(state):
			record = state.reshape(len(state[0]) ** 2)
			record = tuple(record)
			return record

def convertTuple(record):
			board = np.array(record)
			size = int(len(record) ** .5)
			board  = board.reshape(size,size)
			return board
			


	

