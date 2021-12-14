from functools import lru_cache, reduce
from itertools import permutations, combinations
from math import ceil, floor, sqrt, log2
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from collections import deque
from copy import deepcopy

sample = None
s2 = list(el.strip() for el in open("./s2.txt", 'r').readlines())
s3 = list(el.strip() for el in open("./s3.txt", 'r').readlines())
try:
    sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
    pass
except:
    pass

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, s2, s3, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue
    
    ### START CODING HERE -----
    m = {}
    for line in prob:
        l = line.split('-')
        for u, v in ((l[0], l[1]), (l[1], l[0])):
            if u not in m:
                m[u] = set()
            m[u].add(v)

    ind = {}
    for el in m:
        if el == el.lower():
            ind[el] = len(ind)
    dfs = [("start", 0, i, False) for i in range(len(ind)) if i not in [ind["start"], ind["end"]]]
    dfs.append(("start", 0, None, True))
    ret = 0
    while dfs:
        cur, bs, dbl, used = dfs.pop()
        if cur == "end":
            ret += used and (dbl is None or (bs >> dbl) & 1 == 1)
            continue
        
        if cur == cur.lower():
            index = ind[cur]
            if (bs >> index) & 1:
                continue
            elif index == dbl and not used:
                used = True
            else:
                bs |= (1 << index)

       
        for neigh in m[cur]:
            dfs.append((neigh, bs, dbl, used))

    print(ret)
