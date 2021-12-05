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
    for el in prob:
        l = el.split("->")
        s = []
        zeroComma = l[0].find(',')
        oneComma = l[1].find(',')
        s.append(int(l[0][:zeroComma]))
        s.append(int(l[0][zeroComma+1:]))

        e = []
        e.append(int(l[1][:oneComma]))
        e.append(int(l[1][oneComma+1:]))

        inc = [0, 0]
        if s[0] != e[0]:
            inc[0] = 1 if s[0] < e[0] else -1
        if s[1] != e[1]:
            inc[1] = 1 if s[1] < e[1] else -1
        while s != e:
            imm = tuple(s)
            ct[imm] = ct.get(imm, 0) + 1
            s[0] += inc[0]
            s[1] += inc[1]
        imm = tuple(s)
        ct[imm] = ct.get(imm, 0) + 1


    print(sum(ct[el] > 1 for el in ct))

