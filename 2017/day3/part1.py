from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

sample = None
try:
    pass
    #sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
except:
    pass

mine = list(el.strip() for el in open("./input.txt", 'r').readlines())

for prob in [sample, mine]:
    if not prob or not prob[0]:
        continue

    def s(coords):
        return sum(abs(c) for c in coords)

    i = 0
    for n in map(int, prob):
        while (2*i + 1)**2 < n:
            i += 1

        coords = [i, i]
        add = [(0, -1), \
               (-1, 0), \
               (0, 1), \
               (1, 0)]
        num = (2*i + 1)**2
        for di, dj in add:
            ti = 0 if di else 1
            target = i * (-1 if min(di, dj) < 0\
                             else 1)
            while n != num and \
                  coords[ti] != target:
                coords[ti] += (1 if target > 0 else -1)
                num -= 1

            if n == num:
                print(s(coords))
                break
