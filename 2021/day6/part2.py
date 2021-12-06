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
    l = list(map(int, prob[0].split(',')))
    ct = {}
    for el in l:
        ct[el] = ct.get(el, 0) + 1

    for i in range(256):
        new = {}
        for el in ct:
            if el == 0:
                new[6] = new.get(6, 0) + ct[el]
                new[8] = new.get(8, 0) + ct[el]
            else:
                new[el-1] = new.get(el-1, 0) + ct[el]
        ct = new

    
    print(sum(ct[el] for el in ct))
