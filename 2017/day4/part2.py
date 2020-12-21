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
    ret = 0
    for line in prob:
        seen = {}
        for w in line.split(' '):
            srt = ''.join(sorted(w))
            seen[srt] = seen.get(srt, 0) + 1

        ret += all(seen[srt] == 1 for srt in seen)
    print(ret)
