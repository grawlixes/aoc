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

    def s(coords):
        return sum(abs(c) for c in coords)

    m = {}
    i, j = 0, 1
    m[(0,0)] = 1
    l = 1
    add = [-1,0]
    for n in map(int, prob):
        while True:
            v = sum(m.get((i+i2,j+j2), 0) for i2 in range(-1,2) \
                                          for j2 in range(-1,2))

            if v > n:
                print(v)
                break
            
            m[(i,j)] = v

            if s((i, j)) == 2*l:
                if add[0]:
                    add = [0, add[0]]
                else:
                    add = [-add[1], 0]
                
            if i + j == 2*l:
                j += 1
                l += 1
            else:
                i, j = i + add[0], j + add[1]
            
