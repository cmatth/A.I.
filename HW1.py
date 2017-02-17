# Casey Matthews
# Artifical Intelligence
# Homework 1

import NPuzzle as puz
import Search
from subprocess import call
import time

call(["clear"])
puzzle = puz.newPuzzle(4)

print "DepthFirst Tuples:\n"
start = time.time()
answer = Search.GraphSearch(puzzle, puz.solved, puz.children, Search.DepthFirstT)
stop = time.time()
print "\nSeconds: %d" %(stop - start)


print "BreadthFirst Tuples:\n"
start = time.time()
answer = Search.GraphSearch(puzzle, puz.solved, puz.children, Search.BreadthFirstT)
stop = time.time()
print "\nSeconds: %d" %(stop - start)

'''
print "\n*** NxN Puzzle ***"
puz.show()
print "*******************"
for x in answer:
	print x
'''

'''
if answer[0] == True:
	print "\nSolution found:"
	print answer[1]
else:
	print "Failed to find answer."

print "\n******************"
'''
