from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque
from copy import deepcopy

sample = None
try:
    #sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
    pass
except:
    pass

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue

    p1 = deque()
    i = 1
    while prob[i] != '':
        p1.append(int(prob[i]))
        i += 1

    p2 = deque()
    i += 2
    while i < len(prob):
        p2.append(int(prob[i]))
        i += 1

    while p1 and p2:
        if p1[0] > p2[0]:
            p1.append(p1.popleft())
            p1.append(p2.popleft())
        else:
            p2.append(p2.popleft())
            p2.append(p1.popleft())

    final = p1 if p1 else p2
    print(sum(final[i] * (len(final) - i) for i in range(len(final))))
