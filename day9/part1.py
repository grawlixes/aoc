from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

length = 25 
have = deque()
for i,line in enumerate(l):
    n = int(line)
    have.append(n)

    if len(have) > length:
        if not any(have[i] + have[j] == n for i in range(length) for j in range(i + 1, length)):
            print(n)
            break
        
        have.popleft()

