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

def arith(n):
    return n * (n + 1) // 2

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue
    
    ### START CODING HERE -----
    l = list(map(int, prob[0].split(',')))
    s = sorted(l)
    ret = 0
    mi, ma = min(l), max(l)
    m = {el:0 for el in range(mi, ma + 1)}
    for el in l:
        for i in range(mi, ma + 1):
            m[i] += arith(abs(i - el))

    best = 0
    for el in m:
        if m[el] < m[best]:
            best = el

    print(m[best])
