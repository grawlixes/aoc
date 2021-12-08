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
    ct = {}
    m = {2: 1, 4: 4, 3: 7, 7: 8}

    for line in prob:
        line = line[line.index('|')+2:]
        l = line.split(' ')
        for el in l:
            if len(el) in m:
                v = m[len(el)]
                ct[v] = ct.get(v, 0) + 1
    print(sum(ct.values()))

