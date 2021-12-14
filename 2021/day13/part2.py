from functools import lru_cache, reduce
from itertools import permutations, combinations
from math import ceil, floor, sqrt, log2
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from collections import deque
from copy import deepcopy

sample = None
try:
    sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
    pass
except:
    pass

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue
    
    ### START CODING HERE -----
    points = set()
    for line in prob:
        if len(line) == 0:
            break
        x, y = map(int, line.split(','))
        points.add((x, y))
        
    i = prob.index('') + 1
    while i < len(prob):
        new = set()
        inst = prob[i].split(' ')[2]
        v = int(inst.split('=')[1])
        isX = inst.split('=')[0].lower() == 'x'
        
        for point in points:
            x, y = point
            
            if isX:
                if x > v:
                    x -= 2 * abs(v - x)
            else:
                if y > v:
                    y -= 2 * abs(v - y)

            new.add((x, y))

        points = new
        i += 1
    minx = min(point[0] for point in points)
    maxx = max(point[0] for point in points)
    miny = min(point[1] for point in points)
    maxy = max(point[1] for point in points)

    l = []
    for y in range(miny, maxy + 1):
        line = []
        for x in range(minx, maxx + 1):
            p = (x, y)
            line.append('#' if p in points else '.')
        print(''.join(line))
