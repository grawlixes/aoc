from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

sample = None
mine = list(el.strip() for el in open("./input.txt", 'r').readlines())

for prob in [sample, mine]:
    if not prob or not prob[0]:
        continue

    cs = 0
    for l in prob:
        mi, ma = float('inf'), -float('inf')
        for n in map(int, l.split('\t')):
            print(n)
            mi = min(mi, n)
            ma = max(ma, n)

        cs += ma - mi

    print(cs)
