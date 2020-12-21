from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

sample = None
try:
    #pass
    sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
except:
    pass

mine = list(el.strip() for el in open("./input.txt", 'r').readlines())

for prob in [sample, mine]:
    if not prob or not prob[0]:
        continue

    # START CODING HERE
    prob = list(map(int, prob))
    i = 0
    steps = 0
    while i >= 0 and i < len(prob):
        ti = i + prob[i]
        if prob[i] >= 3:
            prob[i] -= 1
        else:
            prob[i] += 1
        i = ti
        steps += 1

    print(steps)
