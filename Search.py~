# Casey Matthews
# Artificial Intelligence Spring 2017
# Search Algorithms

import numpy as np
import Queue
import NPuzzle as p


def BreadthFirst(root, verifier, children):
	Open = [] 
	Open.append(root)
	closed   = []
	solution = False
	visited = False

	while not len(Open) == 0:
		state = Open[0]
		Open.remove(state)
		solution = verifier(state)
		
		if solution == False:
			closed.append(state)
			newChil = children(state)
	
			for x in newChil:
				if x != -1
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
			
		

def GraphSearch(config, verify, makeChildren, searchAlgorithm):
	return searchAlgorithm(config, verify, makeChildren)
	

