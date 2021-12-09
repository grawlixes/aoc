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
    ret = 0
    n, m = len(prob), len(prob[0])
    lp = []
    for i in range(n):
        for j in range(m):
            neigh = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]

            succ = True
            for i2, j2 in filter(lambda tup: min(tup) >= 0 and tup[0] < n and tup[1] < m,neigh):
                if prob[i][j] >= prob[i2][j2]:
                    succ = False
                    break

            if succ:
                lp.append((i, j))

    sizes = []
    seen = set()
    for tup in lp:
        if tup in seen:
            continue
        search = [tup]
        size = 0
        while search:
            t = search.pop()
            if t in seen:
                continue
            seen.add(t)
            size += 1
            i, j = t
            
            neigh = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            for i2, j2 in filter(lambda tup: min(tup) >= 0 and tup[0] < n and tup[1] < m,neigh):
                if prob[i2][j2] != '9' and prob[i2][j2] > prob[i][j]:
                    search.append((i2, j2))

        sizes.append(size)
    sizes.sort(reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])
