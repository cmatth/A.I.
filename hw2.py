# Casey Matthews
# Artificial Intelligence
# Homework 2
# N-Queens Hill Climbing

import numpy
import nqueens
import graph
import Search



size = 4
Nqueens = graph.Graph(nqueens, nqueens.solvedNew, Search.BreadthFirstT, size)
Nqueens.search()
