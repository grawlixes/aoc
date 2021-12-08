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
    m = {2: 1, 4: 4, 3: 7, 7: 8}
    ret = 0
    for line in prob:
        typ = {}
        i = line.index('|')
        ten = line[:i-1]
        four = line[i+2:]
        t = ten.split(' ')
        for el in t:
            if len(el) in m:
                v = m[len(el)]
                typ[v] = el
        
        f = four.split(' ')
        cur = []
        for el in f:
            if len(el) in m:
                cur.append(m[len(el)])
            elif all(ch in el for ch in typ[4]):
                cur.append(9)
            elif all(ch in el for ch in typ[7]):
                if len(el) == 5:
                    cur.append(3)
                else:
                    cur.append(0)
            elif len(el) == 5:
                if sum(ch in el for ch in typ[4]) == 3:
                    cur.append(5)
                else:
                    cur.append(2)
            else:
                cur.append(6)
        ret += int(''.join(map(str, cur)))
    print(ret)

