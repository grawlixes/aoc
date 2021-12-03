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
    j = 0
    i = 0
    aim = 0
    for el in prob:
        s = el.split()
        d = s[0]
        v = int(s[1])

        if d == "forward":
            j += v
            i += aim * v
        elif d == "down":
            aim += v
        elif d == "up":
            aim -= v

    print(i * j)
