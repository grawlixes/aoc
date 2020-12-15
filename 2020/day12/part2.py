from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

l = list(el.strip() for el in open("./input.txt", 'r').readlines())
pos = [0, 0]
wp = [10, 1]

for line in l:
    d = line[0].upper()
    mag = int(line[1:])

    if d == 'L':
        # I forgot to loop this for like 20 minutes
        for _ in range(mag // 90):
            wp = [-wp[1], wp[0]]
    elif d == 'R':
        for _ in range(mag // 90):
            wp = [wp[1], -wp[0]]
    elif d != 'F':
        if d == 'N':
            wp[1] += mag
        elif d == 'S':
            wp[1] -= mag
        elif d == 'W':
            wp[0] -= mag
        elif d == 'E':
            wp[0] += mag
        else:
            print("weird", line)
    else:
        pos[0] += wp[0] * mag
        pos[1] += wp[1] * mag

print(abs(pos[0]) + abs(pos[1]))
