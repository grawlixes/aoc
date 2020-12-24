from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque
from copy import deepcopy

sample = None
try:
    #sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
    pass
except:
    pass

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue

    black = set()
    for line in prob:
        i = 0
        pos = [0, 0]
        while i < len(line):
            command = line[i] if line[i] in "ew" else line[i:i+2]
            if command in "ew":
                pos[0] += -2 if command == 'w' else 2
            else:
                pos[0] += -1 if command[1] == 'w' else 1
                pos[1] += -1 if command[0] == 's' else 1
            i += len(command)

        t = tuple(pos)
        if t in black:
            black.remove(t)
        else:
            black.add(t)

    print(len(black))
