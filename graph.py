import numpy
from collections import deque

class Graph():
	def __init__(self, problem, evalFun, searchFun, size):
		self.problem = problem
		self.evalFun = evalFun
		self.searchFun = searchFun
		self.root = Node(problem.getInitialState(size))
		self.Open = deque()
    		self.closed = set([])
    		self.solutions = []

	def search(self):
		print "Hubba bubba"
		
class Node():

	def __init__(self, state, parent=None):
		if parent != None: self.generation = parent.generation + 1
		else: self.generation = 0
		self.content = state
	
			
		
		
		
		
