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
    prev = None
    ret = 0
    for num in map(int, c):
        ret += (prev == num) * num
        prev = num
    ret += (prev == int(c[0])) * prev

    print(ret)
