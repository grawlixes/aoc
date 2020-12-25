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

    cardKey = int(prob[0])
    doorKey = int(prob[1])
    mod = 20201227

    cardLoop = 0
    cur = 1
    while cur != ck:
        cur = (cur * 7) % mod
        cardLoop += 1

    cur = 1
    for _ in range(cardLoop):
        cur = (cur * doorKey) % mod

    print(cur)
