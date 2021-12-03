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
    l = len(prob[0])
    tot = [{'0': 0, '1': 0} for _ in range(l)]
    for line in prob:
        for i,b in enumerate(line):
            tot[i][b] += 1

    gamma = sum(1 << (l - i - 1) if max(tot[i].values()) == tot[i]['1'] else 0 for i in range(l))
    epsilon = (1 << l) - gamma - 1
    print(gamma * epsilon)
