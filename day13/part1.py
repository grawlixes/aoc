from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

earliest = int(l[0])
busStr = l[1]

bestBus, mins = -1, float('inf')
for b in busStr.split(','):
    if b == 'x':
        continue
    id = int(b)
    ogId = id
    while id < earliest:
        id += ogId

    if id < mins:
        bestBus, mins = ogId, id

print(bestBus * (mins - earliest))
