from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

need = 1309761972
have = deque()
s = 0
for i,line in enumerate(l):
    n = int(line)
    s += n
    have.append(n)

    while s > need:
        s -= have.popleft()

    if s == need and len(have) >= 2:
        print(max(have) + min(have))
        break
