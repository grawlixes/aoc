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
    temp = prob[0]
    i = 2
    rules = {}
    while i < len(prob):
        r, o = prob[i].split('->')
        rules[r.strip()] = o.strip()
        i += 1

    stack = []
    for i in range(10):
        new = [temp[0]]
        for i in range(len(temp) - 1):
            s = temp[i] + temp[i+1]
            if s in rules:
                new.append(rules[s])
            new.append(temp[i+1])

        temp = ''.join(new)
    mc, lc = 'N', 'N'
    for el in set(temp):
        c = temp.count(el)
        if c > temp.count(mc):
            mc = el
        if c < temp.count(lc):
            lc = el
    print(temp.count(mc) - temp.count(lc))
