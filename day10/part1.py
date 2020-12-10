from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

l = sorted(list(map(int, l)))

cur = 0
ones = 0
# three at the end counts
threes = 1
for i in range(len(l)):
    if l[i] > cur + 3:
        break
    if l[i] == cur:
        continue

    ones += l[i] == (cur + 1)
    threes += l[i] == (cur + 3)
    cur = l[i]

print(ones * threes)
