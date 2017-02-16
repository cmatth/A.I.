# Casey Matthews
# Artifical Intelligence
# Homework 1

import NPuzzle as puz
import Search

puzzle = puz.newPuzzle(3)
#puz.show()
answer = Search.GraphSearch(puzzle, puz.solved, puz.children, Search.BreadthFirst)
if answer[0] == True:
	print "Solution found:\n"
	print answer[1]
else:
	print "Failed to find answer."
