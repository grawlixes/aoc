from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

# this one isn't so bad, it's less than 2 seconds on my machine

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

nxt = [['.' for _ in range(len(l[0]))] for _ in range(len(l))]

seen = {}

for i in range(len(l)):
    for j in range(len(l[i])):
        seen[(i, j)] = set()

        dfs = [(i + k, j + k2, k, k2) \
               for k in range(-1, 2) \
               for k2 in range(-1, 2) \
               if (k != 0 or k2 != 0)]

        while dfs:
            i2, j2, k, k2 = dfs.pop()
            if min(i2, j2) < 0 or \
               i2 == len(l) or \
               j2 == len(l[0]):
                   continue
            
            if l[i2][j2] != '.':
                seen[(i, j)].add((i2, j2))
                continue

            dfs.append((i2 + k, j2 + k2, k, k2))

occ = [0, 0]
while True:
    for i in range(len(l)):
        for j in range(len(l[i])):
            adjFull = sum(l[i2][j2] == '#' for i2,j2 in seen[(i, j)])
            
            if l[i][j] == 'L':
                nxt[i][j] = '#' if adjFull == 0 else 'L'
            elif l[i][j] == '#':
                nxt[i][j] = 'L' if adjFull >= 5 else '#'
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
