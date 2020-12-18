from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
mine = list(el.strip() for el in open("./input.txt", 'r').readlines())

for prob in [sample, mine]:
    if not prob or not prob[0]:
        continue

    c = prob[0]
    nxt = len(c) // 2
    ret = 0
    a = list(map(int, c))
    for i, num in enumerate(a):
        ret += (num == a[(i + nxt) % len(a)]) * num
        prev = num
    
    print(ret)
