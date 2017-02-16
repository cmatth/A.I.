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
		Progress(count)
		
		if solution == False:
			closed.append(state)
			newChil = children(state)
	
			for x in newChil:
				if type(x) is np.ndarray:
					visited = False
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
		else:
			return [True, state]
	return [False, "No solution found."]
			
def Progress(count):
	progress = (count / space) * 100
	print 'Space Traversed [%d%%]\r'%progress,


	

