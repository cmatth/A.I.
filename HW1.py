# Casey Matthews
# Artifical Intelligence
# Homework 1

import NPuzzle as puz
import nqueens as queens
import Search
from subprocess import call
import time

call(["clear"])
print "DepthFirst Queens:"
puzzle = queens.newBoard(7)
#print puzzle
start = time.time()
answer = Search.GraphSearch(puzzle, queens.solved, queens.getChildren, Search.DepthFirstT, queens.spaceSize)
stop = time.time()
print "\nSeconds: %d" %(stop - start)
#print answer




puzzle = puz.newPuzzle(3)
print "\nDepthFirst Puzzle:"
start = time.time()
answer = Search.GraphSearch(puzzle, puz.solved, puz.children, Search.DepthFirstT, puz.spaceSize)
stop = time.time()
print "\nSeconds: %d" %(stop - start)

'''
print "BreadthFirst Tuples:\n"
start = time.time()
answer = Search.GraphSearch(puzzle, puz.solved, puz.children, Search.BreadthFirstT)
stop = time.time()
print "\nSeconds: %d" %(stop - start)
'''

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
