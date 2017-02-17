# Casey Matthews
# Artifical Intelligence
# Homework 1

import NPuzzle as puz
import Search
from subprocess import call

call(["clear"])
puzzle = puz.newPuzzle(3)
answer = Search.GraphSearch(puzzle, puz.solved, puz.children, Search.BreadthFirstT)

print "\n*** NxN Puzzle ***"
puz.show()
print "*******************"
for x in answer:
	print x
'''
if answer[0] == True:
	print "\nSolution found:"
	print answer[1]
else:
	print "Failed to find answer."

print "\n******************"
'''
