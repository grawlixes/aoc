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
except:
    pass

def printGrid(prob):
    for row in prob:
        print(''.join(row))
    print('\n')
personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for it,prob in enumerate([sample, personal]):
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue
    
    ### START CODING HERE -----
    prob = [list(el) for el in prob]
    n = len(prob) 
    flashes = 0    
    for _ in range(100):
        for j in range(n):
            for k in range(n):
                prob[j][k] = str(min(int(prob[j][k]) + 1, 10))

        tens = [(i, j) for i in range(n) for j in range(n) if prob[i][j] == '10']
        visited = set()
        while tens:
            i, j = tens.pop()
            tup = (i, j)
            if tup in visited:
                continue
            visited.add(tup)
            prob[i][j] = '0'
            flashes += 1
            
            neigh = [(i + k, j + l) for k in range(-1, 2) for l in range(-1, 2) if k != 0 or l != 0]
            for i2, j2 in filter(lambda tup: min(tup) >= 0 and max(tup) < n and tup not in visited, neigh):
                prob[i2][j2] = str(min(10, int(prob[i2][j2]) + 1))
                if prob[i2][j2] == '10':
                    tens.append((i2, j2))
     
    print(flashes)
