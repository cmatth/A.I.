# Casey Matthews
# Artifical Intelligence
# Homework 1

import NPuzzle as puz
import Search

puzzle = puz.newPuzzle(3)
puz.show()
print Search.GraphSearch(puzzle, puz.solved, puz.children, Search.BreadthFirst)
