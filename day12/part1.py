from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

pos = [0, 0]
direction = ['E', 'S', 'W', 'N']
facing = 0

for line in l:
    d = line[0]
    mag = int(line[1:])

    if d in "LR":
        facing = (facing + (mag // 90) * (1 if d == 'R' else -1)) % 4
    else:
        d = d if d != 'F' else direction[facing]
        if d == 'N':
            pos[1] += mag
        elif d == 'S':
            pos[1] -= mag
        elif d == 'W':
            pos[0] -= mag
        elif d == 'E':
            pos[0] += mag
        else:
            print("weird", line)

print(abs(pos[0]) + abs(pos[1]))
