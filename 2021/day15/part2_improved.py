# This isn't code that I ran during the contest, but I think it
# would have been a lot faster to implement if I did.
# Compare it to the code I wrote in part2.py.

from functools import lru_cache, reduce
from itertools import permutations, combinations
from math import ceil, floor, sqrt, log2
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from collections import deque
from copy import deepcopy

sample = None
try:
    sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
    pass
except:
    pass

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue
    
    ### START CODING HERE -----
    heap = [(0, 0, 0)]
    visited = set()
    n, m = len(prob), len(prob[0])
    while heap:
        cost, i, j = heappop(heap)

        tup = (i, j)
        if tup in visited:
            continue
        if tup == (5*n - 1, 5*m - 1):
            print(cost)
            break
        visited.add(tup)
    
        neigh = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
        for i2, j2 in filter(lambda tup: min(tup) >= 0 and tup[0] < 5*n and tup[1] < 5*m, neigh):
            
            this = int(prob[i2 % n][j2 % m])
            
            ti, tj = i2, j2
            while ti >= n:
                this += 1
                if this == 10:
                    this = 1
                ti -= n
            while tj >= m:
                this += 1
                if this == 10:
                    this = 1
                tj -= m

            heappush(heap, (cost + this, i2, j2))

    
