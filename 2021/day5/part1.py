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

        if s[0] != e[0] and s[1] != e[1]:
            continue

        inc = [0, 0]
        cur = None
        lim = None
        if s[0] == e[0]:
            inc[1] += 1
            cur = [s[0], min(e[1], s[1])]
            lim = [s[0], max(e[1], s[1])]
        else:
            inc[0] += 1
            cur = [min(e[0], s[0]), e[1]]
            lim = [max(e[0], s[0]), e[1]]
        print(cur, lim)
        while cur != lim:
            imm = tuple(cur)
            ct[imm] = ct.get(imm, 0) + 1
            cur[0] += inc[0]
            cur[1] += inc[1]
        imm = tuple(cur)
        ct[imm] = ct.get(imm, 0) + 1


    print(ct)
    print(sum(ct[el] > 1 for el in ct))

