import numpy as np
import copy
import operator
import random
import time

class State:
	def __init__(self, seed):
		self.seed  = seed
		self.score = evaluate(seed)


def evaluate(seed):
	clashes = 0
	row_col_clashes = abs(_size - len(np.unique(seed)))
	clashes += row_col_clashes

	# calculate diagonal clashes
	for i in range(_size):
		for j in range(_size):
			if ( i != j):
				dx = abs(i-j)
				dy = abs(seed[i] - seed[j])
				if(dx == dy):
					clashes += 1
	return clashes

def makeState(seed):
	state = np.zeros(_size**2).reshape(_size, _size)
	
	for x in range(0,_size):
		state[seed[x], x] = 1

	print state

def replenishPop(pop):
	#raw_input("breeding")
	size = len(pop) - 2
	
	x = 0
	while x < size:
		mother = pop[x]
		father = pop[x+1]
		childs = breed(mother, father)
		for y in childs:
			pop.append(y)
		x += 2
	return pop


def breed(p1,p2):
	mutRate = 30
	crossover = np.random.randint(0, _size, 1)
	childseed1 = copy.copy(p1.seed)
	childseed2 = copy.copy(p2.seed)
	for x in range(crossover, _size):
		childseed1[x] = p2.seed[x]
		childseed2[x] = p1.seed[x]

	#roll for mutation
	if np.random.randint(1, 100, 1) > mutRate:
		gene1 = np.random.randint(0, _size, 1)
		gene2 = np.random.randint(0, _size, 1)
		tmp = childseed1[gene1]
		childseed1[gene1] = childseed1[gene2]
		childseed1[gene2] = tmp

	#roll for mutation
	if np.random.randint(1, 100, 1) > mutRate:
		gene1 = np.random.randint(0, _size, 1)
		gene2 = np.random.randint(0, _size, 1)
		tmp = childseed2[gene1]
		childseed2[gene1] = childseed2[gene2]
		childseed2[gene2] = tmp

	if len(childseed1) > len(np.unique(childseed1)):
		#print "repairing", childseed1
		
		childseed1 = repair(childseed1)

		#print "repaired:", childseed1
		#raw_input("ENTER")

	if len(childseed2) > len(np.unique(childseed2)):
		childseed2 = repair(childseed2)

	return State(childseed1), State(childseed2)

def repair(seed):
	a = np.arange(0,_size)
	for x in seed:
		index = np.argwhere(a==x)
		a = np.delete(a,index)
	#print a
	if len(a) > 0:
		for y in range(0,_size):
			indices = [i for i, x in enumerate(seed) if x == y]
			if len(indices) > 1:
				num = np.random.randint(0,len(indices))
				seed[indices[num]] = a[0]
				np.delete(a,0)
			if len(a) == 0:
				break
	return seed

popSize = 150
_size = 100
maxGenerations = 400

pop1 = []
pop  = []

run = False
start = time.time()
while(run):
	for x in range(0,popSize):
		pop1.append(np.arange(0,_size))

	for x in pop1:
		random.shuffle(x)
		pop.append(State(x))


	generation = 0
	raw_input("Restarting")
	while(run and generation <= maxGenerations):
		popscore = 0

		if pop[0].score == 0:
			stop = time.time()
			run = False
			print "Solved"
			print pop[0].seed, pop[0].score
			print "Time Taken: %d sec" %(stop - start)
			break

		#kill off weaker half
		#pop = pop[:(popSize / 2)]
		#print len(population)

		'''
		print "original*************************"
		for x in pop:
			print x.seed, x.score,':', len(x.seed) - len(np.unique(x.seed))
			popscore += x.score
		'''
		print "gen: %d" %generation

		#breed population randomly
		random.shuffle(pop)
		pop = replenishPop(pop)
		
		#reduce pop to original size
		pop = sorted(pop, key=operator.attrgetter("score"), reverse=False)

		pop = pop[:popSize]
		generation += 1


chr =  State([66, 39, 73, 55, 64, 72, 21, 75, 20, 90, 27, 97, 45,  6, 57,  5, 38, 89, 77, 46, 84, 82, 52, 71, 78,
		 10, 36, 18, 22, 24, 87, 76, 53, 34, 14,  8, 13, 61, 67, 58, 29, 11, 28, 98, 79, 92, 50, 43, 94, 23,
		 63, 95,  4, 35, 74, 81, 62, 91, 99, 56,  0, 25, 60, 47, 96, 16, 26,  9, 70, 31, 88,  7, 19, 41, 15,
		 12, 85,  2, 33, 48, 59, 44,  1, 86, 17, 93, 30, 32, 80, 37,  3, 40, 42, 54, 69, 49, 83, 68, 51, 65] )

makeState(chr.seed)

