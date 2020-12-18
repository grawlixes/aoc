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
    N *= 2
    m, n = len(prob), len(prob[0])
    states = [[['.' for _ in range(n + N + 2)] for _ in range(m + N + 2)] for _ in range(N + 1)]
    for i in range(len(prob)):
        for j in range(len(prob[i])):
            states[0][i + N//2][j + N//2] = prob[i][j]

    active = None
    # START CODING HERE
    for c in range(6):
        nxt = deepcopy(states) 
        active = 0
        for i in range(len(states) - 1):
            for j in range(1, len(states[0]) - 1):
                for k in range(1, len(states[1]) - 1):
                    neigh = 0
                    for i2 in range(-1, 2):
                        for j2 in range(-1, 2):
                            for k2 in range(-1, 2):
                                if (i2 or j2 or k2) and states[abs(i + i2)][j + j2][k + k2] == '#':
                                        neigh += 1

                    if (states[i][j][k] == '#' and neigh in [2, 3]) or \
                       (states[i][j][k] == '.' and neigh == 3):
                           nxt[i][j][k] = '#'
                           active += 1 + (i > 0)
                    else:
                        nxt[i][j][k] = '.'

        states = nxt

    print(active)
