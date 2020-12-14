from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

mem = {}
mask = None
for line in l:
    if line[:4] == "mask":
        ms = line[line.index("= ") + 2:]
        mask = [0 for _ in range(len(ms))]

        for i in range(len(ms)):
            if ms[i] in ['1', '0']:
                mask[i] = int(ms[i])
            else:
                mask[i] = -1
    else:
        j = int(line[line.index('[') + 1:\
                     line.index(']')])
        val = int(line[line.index('= ') + 2:])
        for i in range(len(mask)):
            bit = len(mask) - i - 1
            if mask[i] == 1:
                val |= 1 << bit
            elif mask[i] == 0:
                if (val >> bit) & 1:
                    val -= 1 << bit

        mem[j] = val

print(sum(mem.values()))
