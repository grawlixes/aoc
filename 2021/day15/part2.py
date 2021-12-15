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
    og = [el[:] for el in prob]

    for i in range(4):
        for ri in range(n):
            for el in prob[ri][len(prob[ri]) - m:]:
                nxt = int(el) + 1
                nxt = 1 if nxt == 10 else nxt
                prob[ri] += str(nxt)

    
    for it in range(4):
        for i in range(n):
            l = []
            for rj in range(5*m):
                ti = it*n + i
                nxt = int(prob[ti][rj]) + 1
                nxt = 1 if nxt == 10 else nxt
                l.append(str(nxt))

            prob.append(''.join(l))

    n *= 5
    m *= 5
    while heap:
        cost, i, j = heappop(heap)
        tup = (i, j)
        if tup in visited:
            continue
        if tup == (n - 1, m - 1):
            print(cost)
            break
        visited.add(tup)
    
        neigh = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
        for i2, j2 in filter(lambda tup: min(tup) >= 0 and tup[0] < n and tup[1] < m, neigh):
            heappush(heap, (cost + int(prob[i2][j2]), i2, j2))

    
