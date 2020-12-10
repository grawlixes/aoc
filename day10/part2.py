from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

l = sorted(list(map(int, l)))
l = [0] + l

cur = 0
sol = [160]
@lru_cache(None)
def dfs(i):
    if sol[0] - 3 <= l[i]:
        return 1
    j = i + 1
    ret = 0
    while j < len(l) and l[j] <= l[i] + 3:
        ret += dfs(j)
        j += 1
    return ret
print(dfs(0))
