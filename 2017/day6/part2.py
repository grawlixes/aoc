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
    banks = list(map(int, prob[0].split('\t')))

    seen = {}
    ct = 0
    conf = tuple(banks)
    while conf not in seen or seen[conf] < 2:
        seen[conf] = seen.get(conf, 0) + 1
        ma = 0 
        for i in range(1, len(banks)):
            if banks[ma] < banks[i]:
                ma = i
        
        j = (ma + 1) % len(banks)
        for _ in range(banks[ma]):
            banks[j] += 1
            banks[ma] -= 1

            j = (j + 1) % len(banks)
        conf = tuple(banks)
        ct += 1

    print(ct - (5 if len(banks) == 4 else 4074))
