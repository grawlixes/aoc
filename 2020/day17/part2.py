from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque
from copy import deepcopy

sample = None
try:
    sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
except:
    pass

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())

for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue

    N = 6
    M = len(prob)
    states = [[[['.' for _ in range(M + N*2 + 4)] for _ in range(M + N*2 + 4)] for _ in range(2*N + 3)] for _ in range(2*N + 3)]
    for i in range(len(prob)):
        for j in range(len(prob[i])):
            states[N+1][N+1][i + N + 2][j + N + 2] = prob[i][j]

    # just fuck me up
    active = None
    # START CODING HERE
    for c in range(6):
        nxt = deepcopy(states) 
        active = 0
        for i in range(1, len(states) - 1):
            for j in range(1, len(states[0]) - 1):
                for k in range(1, len(states[0][0]) - 1):
                    for l in range(1, len(states[0][0][0]) - 1):
                        neigh = 0
                        for i2 in range(-1, 2):
                            for j2 in range(-1, 2):
                                for k2 in range(-1, 2):
                                    for l2 in range(-1, 2):
                                        if (i2 or j2 or k2 or l2) and states[i + i2][j + j2][k + k2][l + l2] == '#':
                                                neigh += 1

                        if (states[i][j][k][l] == '#' and neigh in [2, 3]) or \
                           (states[i][j][k][l] == '.' and neigh == 3):
                               nxt[i][j][k][l] = '#'
                               active += 1
                        else:
                            nxt[i][j][k][l] = '.'

        states = nxt
    
    print(active)
