import numpy as np
import copy
import time

class State:
	def __init__(self, seed):
		self.seed  = seed
		self.score = self.evaluate()


	def evaluate(self):
		clashes = 0
		row_col_clashes = abs(_size - len(np.unique(self.seed)))
		clashes += row_col_clashes

		# calculate diagonal clashes
		for i in range(_size):
			for j in range(_size):
				if ( i != j):
					dx = abs(i-j)
					dy = abs(self.seed[i] - self.seed[j])
					if(dx == dy):
						clashes += 1
		return clashes

	@staticmethod
	def children(self, numSets):
		best = self
		childlist = []
		better = []
		same = []

		for y in range (0, numSets):
			for x in range(0, _size):
				childseed = copy.copy(self.seed)
				childseed[x] = np.random.randint(0, _size, 1)
				childlist.append(State(childseed))

		for x in childlist:
			if x.score < best.score:
				best = x
			if x.score < self.score:
				better.append(x)
			elif x.score == self.score:
				same.append(x)

		if len(better) > 0:
			randy = np.random.randint(0, len(better), 1)
			return better[randy]
		elif len(same) > 0:
			randy = np.random.randint(0, len(same), 1)
			return same[randy]
		else:
			return self

### HILL CLIMBING ################################################
_size = 100
_currentScore = None
restarts = 0
current = State(np.random.randint(0, _size, _size))
print "Starting State:"
print current.seed, ": %d" %(current.score)
start = time.time()
while current.score != 0 and restarts < 30:
	next = State.children(current, 2)
	if next != None:
		print next.seed,": %d" %(next.score)
		current = next
	else:
		restarts += 1
		print "Restarting", restarts
		current = State(np.random.randint(0, _size, _size))

if current.score == 0:
	stop = time.time()
	print "Solved:"
	print current.seed
	print "Time taken: %d sec" %(stop - start)
else:
	print "Failed"

#took 372 seconds
#took 706 seconds