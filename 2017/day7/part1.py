from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

sample = None
try:
    pass
    #sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
except:
    pass

mine = list(el.strip() for el in open("./input.txt", 'r').readlines())

for prob in [sample, mine]:
    if not prob or not prob[0]:
        continue

    # START CODING HERE
    holding = {}
    heldBy = {}
    for line in prob:
        name = line[:line.index(' ')]
        if '->' in line:
            arr = line[line.index('>') + 2:].split(', ')
            holding[name] = set()
            for el in arr:
                heldBy[el] = name
                holding[name].add(el)

    print([el for el in holding if el not in heldBy][0])

