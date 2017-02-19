# Casey Matthews
# Artificial Intelligence Spring 2017
# Search Algorithms

import numpy as np
import Queue
import NPuzzle as p
import nqueens as queens
import math
import time
from collections import deque

# Module Vars
space = 0


def GraphSearch(config, verify, makeChildren, searchAlgorithm, space_size, limit):
    return searchAlgorithm(config, verify, makeChildren, space_size, limit)


def Progress(count):
    Ssize = (count / space)
    print 'Space Traversed [%d%%]\r' % Ssize,


def convertBoard(state):
    record = state.reshape(len(state[0]) ** 2)
    record = tuple(record)
    return record


def convertTuple(record):
    board = np.array(record)
    size = int(len(record) ** .5)
    board = board.reshape(size, size)
    return board


def BreadthFirstT(root, verifier, children, space_size, depthLimit=0):
    Open = deque()
    closed = set([])
    solutions = []
    Open.append(convertBoard(root))
    solution = False
    found = False
    global space
    space = space_size()

    while not len(Open) == 0:
        # get matrix and tuple representations from Open
        # then remove from open
        record = Open.popleft()
        state = convertTuple(record)

        # Check if state is a solution
        solution = verifier(state)

        # Progress
        Progress(len(closed))

        if solution == False:
            if record not in closed:
                closed.add(record)
            newChil = children(state)

            # check if any new children are repeated states
            for x in newChil:
                if type(x) is np.ndarray:
                    x = convertBoard(x)
                    if x not in closed:
                        Open.append(x)

        else:

            for s in solutions:
                if p.compare(state, s) == True:
                    found = True
                    break
            if found == False:
                solutions.append(state)
            else:
                found = False
    return solutions


def DepthFirstT(root, verifier, children, space_size, depthLimit=0):
    Open = deque()
    closed = set([])
    solutions = []
    Open.append(convertBoard(root))
    solution = False
    found = False
    global space
    space = space_size()

    while not len(Open) == 0:
        # get matrix and tuple representations from Open
        # then remove from open
        record = Open.pop()
        state = convertTuple(record)

        # Check if state is a solution
        solution = verifier(state)

        # Progress
        Progress(len(closed))

        if solution == False:
            if record not in closed:
                closed.add(record)
            newChil = children(state)

            # check if any new children are repeated states
            for x in newChil:
                if type(x) is np.ndarray:
                    x = convertBoard(x)
                    if x not in closed:
                        # if x not in Open:
                        Open.append(x)

        else:
            for s in solutions:
                if p.compare(state, s) == True:
                    found = True
                    break
            if found == False:
                solutions.append(state)
            else:
                found = False
    return solutions


def IterativeDeepening(root, verifier, children, space_size, depthLimit=0):
    depth = 0
    solutions = []

    while depth <= depthLimit:
        Open = []
        closed = set([])
        Open.append(convertBoard(root))
        solution = False
        found = False
        global space
        space = space_size()

        # deepening structures
        depthIndices = []
        depthIndices.append(0)
        prntDepth = 0
        print

        while not len(Open) == 0:
            # get matrix and tuple representations from Open
            # then remove from open
            record = Open.pop()
            prntDepth = depthIndices.pop()
            state = convertTuple(record)

            # if not prntDepth <= depth:
            # break

            # Check if state is a solution
            solution = verifier(state)

            # Progress
            Progress(len(closed))

            if solution == False:
                if record not in closed:
                    closed.add(record)
                newChil = children(state)

                # check if any new children are repeated states
                for x in newChil:
                    if type(x) is np.ndarray:
                        x = convertBoard(x)
                        if x not in closed:
                            if prntDepth + 1 <= depth:
                                Open.append(x)
                                depthIndices.append(prntDepth + 1)

            else:
                for s in solutions:
                    if p.compare(state, s) == True:
                        found = True
                        break
                if found == False:
                    solutions.append(state)
                else:
                    found = False
        depth += 1
    return solutions


def BiDirectional(root, verifier, children, space_size, goal):
    Open = []
    GOpen = []
    closed = set([])
    Gclosed = set([])
    # solutions = []
    Open.append(convertBoard(root))
    GOpen.append(convertBoard(goal))
    found = False

    global space
    # space = float(math.factorial(p._size ** 2))
    space = space_size()

    while not len(Open) == 0:
        # get matrix and tuple representations from Open
        # then remove from open
        state = convertTuple(Open[0])
        Gstate = convertTuple(GOpen[0])
        record = Open[0]
        Grecord = GOpen[0]
        Open.remove(record)
        GOpen.remove(Grecord)

        # Check if state is the goal
        if record in Gclosed:
            solution = True
        else:
            solution = False

        # Progress
        Progress(len(closed) + len(Gclosed))

        if solution == False:
            if record not in closed:
                closed.add(record)
                Gclosed.add(Grecord)
            newChil = children(state)
            GChil = children(Gstate)

            # check if any new children are repeated states
            for x in newChil:
                if type(x) is np.ndarray:
                    x = convertBoard(x)
                    if x not in closed:
                        # if x not in Open:
                        Open.append(x)

            # Do the same for goal state
            for x in GChil:
                if type(x) is np.ndarray:
                    x = convertBoard(x)
                    if x not in Gclosed:
                        # if x not in Open:
                        GOpen.append(x)

        else:
            return "Found goal."

    return "The goal state is not reachable from every start configuration. Couldn't find."


def QBiDirectional(root, verifier, children, space_size, goal):
    Open = []
    GOpen = []
    closed = set([])
    Gclosed = set([])
    # solutions = []
    Open.append(convertBoard(root))
    GOpen.append(convertBoard(goal))
    found = False

    global space
    # space = float(math.factorial(p._size ** 2))
    space = space_size()

    while not len(Open) == 0:
        # get matrix and tuple representations from Open
        # then remove from open
        state = convertTuple(Open[0])
        Gstate = convertTuple(GOpen[0])
        record = Open[0]
        Grecord = GOpen[0]
        Open.remove(record)
        GOpen.remove(Grecord)

        # Check if state is the goal
        if record in Gclosed:
            solution = True
        else:
            solution = False

        # Progress
        Progress(len(closed) + len(Gclosed))

        if solution == False:
            if record not in closed:
                closed.add(record)
                Gclosed.add(Grecord)
            newChil = children(state, 1)
            GChil = children(Gstate, 0)

            # check if any new children are repeated states
            for x in newChil:
                if type(x) is np.ndarray:
                    x = convertBoard(x)
                    if x not in closed:
                        # if x not in Open:
                        Open.append(x)

            # Do the same for goal state
            for x in GChil:
                if type(x) is np.ndarray:
                    x = convertBoard(x)
                    if x not in Gclosed:
                        GOpen.append(x)

        else:
            return "Found goal."

    return "Did not find."
