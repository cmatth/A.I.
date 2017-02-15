# Casey Matthews
# Artificial Intelligence Spring 2017
# Search Algorithms

import numpy as np
import Queue


def BreadthFirst(root, verifier, children):
	open = Queue.Queue(0) 
	open.put(root)
	closed   = []
	solution = False

	print "before"
	while not open.empty():
		state = open.get()
		solution = verifier(state)
		print "inside"
		
		if solution == False:
			newChil = children(state)
	
			for x in newChil:
				print x
				if not item in open:
					open.put(x)
		else:
			return [True, state]
	return [False, "No solution found."]
			
		

def GraphSearch(config, verify, makeChildren, searchAlgorithm):
	return searchAlgorithm(config, verify, makeChildren)
	

