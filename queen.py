import numpy as np
import copy
import operator
import random

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

def diversify(state)

def breed(p1,p2):
	mutRate = 70
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

	return State(childseed1), State(childseed2)

popSize = 30
_size = 10

pop1 = []
pop  = []

run = True
while(run):
	for x in range(0,popSize):
		pop1.append(np.arange(0,_size))

	for x in pop1:
		random.shuffle(x)
		pop.append(State(x))


	generation = 0
	while(run and generation < 50):	
		popscore = 0


		#raw_input('Press ENTER to continue')

		if pop[0].score == 0:
			run = False
			print "Solved"
			print pop[0].seed, pop[0].score
			break

		#kill off weaker half
		#pop = pop[:(popSize / 2)]
		#print len(population)
		
		print "original"
		for x in pop:
			print x.seed, x.score
			popscore += x.score
		print popscore

		#breed population randomly
		random.shuffle(pop)

		print "breeders"
		for x in pop:
			print x.seed, x.score
			popscore += x.score
		print popscore
		
		pop = replenishPop(pop)

		
		#reduce pop to original size
		pop = sorted(pop, key=operator.attrgetter("score"), reverse=False)

		print "before cull"
		for x in pop:
			print x.seed, x.score
			popscore += x.score
		print popscore

		pop = pop[:popSize]

		#raw_input('Press ENTER to continue')
	print "Random restart"


