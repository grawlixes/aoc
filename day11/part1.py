from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

# should probably optimize this, it takes like 5 seconds

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

nxt = [['.' for _ in range(len(l[0]))] for _ in range(len(l))]

occ = [0, 0]
while True:
    for i in range(len(l)):
        for j in range(len(l[i])):
            adj = [(i + k, j + k2) \
                   for k in range(-1, 1 + 1) \
                   for k2 in range(-1, 1 + 1) \
                   if (i + k != i or j + k2 != j)]
            adjFull = sum(0 \
                          if (min(i2, j2) < 0 or \
                              i2 == len(l) or \
                              j2 == len(l[0])) \
                          else (l[i2][j2] == '#') \
                          for i2,j2 in adj)
            
            if l[i][j] == 'L':
                nxt[i][j] = '#' if adjFull == 0 else 'L'
            elif l[i][j] == '#':
                nxt[i][j] = 'L' if adjFull >= 4 else '#'
            else:
                pass

            occ[1] += nxt[i][j] == '#'

    if occ[0] == occ[1]:
        print(occ[0])
        break
    occ[0] = occ[1]
    occ[1] = 0
    l = nxt
    nxt = [['.' for _ in range(len(l[0]))] for _ in range(len(l))]
