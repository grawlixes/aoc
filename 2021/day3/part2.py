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

    s = set(prob)
    o = None
    i = 0
    while len(s) > 1:
        new = set()
        moreCommon = '1' if max(tot[i].values()) == tot[i]['1'] else '0'
        s = set(el for el in s if el[i] == moreCommon)
        i += 1
        tot = [{'0': 0, '1': 0} for _ in range(l)]
        for line in s:
            for j,b in enumerate(line):
                tot[j][b] += 1
   
    el = s.pop()
    o = sum(1 << (l - i - 1) if el[i] == '1' else 0 for i in range(l))

    s = set(prob)
    i = 0
    while len(s) > 1:
        new = set()
        moreCommon = '0' if max(tot[i].values()) == tot[i]['1'] else '1'
        s = set(el for el in s if el[i] == moreCommon)
        i += 1
        tot = [{'0': 0, '1': 0} for _ in range(l)]
        for line in s:
            for j,b in enumerate(line):
                tot[j][b] += 1
   
    el = s.pop()
    c = sum(1 << (l - i - 1) if el[i] == '1' else 0 for i in range(l))
    print(o*c)
