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

def checkWinners(has):
    for it in range(len(has)):
        h = has[it]
        if any(all((i, j) in h for i in range(5)) for j in range(5)):
            return it
        if any(all((i, j) in h for j in range(5)) for i in range(5)):
            return it
    
    return -1

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue
    
    ### START CODING HERE -----
    numbers = prob[0].split(',')
    i = 2
    boards = []
    loc = []
    while i < len(prob):
        lines = []
        for j in range(i, i + 5):
            lines.append([el for el in prob[j].strip().split(' ') if len(el) > 0])
        i += 6
        boards.append(lines)
        loc.append({})
        for k in range(5):
            for j in range(5):
                loc[-1][boards[-1][k][j]] = (k, j)
    has = [set() for _ in boards]
    for n in numbers:
        for i,b in enumerate(boards):
            if n in loc[i]:
                has[i].add(loc[i][n])

        wbi = checkWinners(has)
        while len(boards) > 1 and wbi != -1:
            boards.pop(wbi)
            loc.pop(wbi)
            has.pop(wbi)
            wbi = checkWinners(has)

        if len(boards) == 1 and checkWinners(has) == 0:
            wbi = 0
            wb = boards[0]
            unmarked = 0
            for i in range(5):
                for j in range(5):
                    if (i, j) not in has[wbi]:
                        unmarked += int(wb[i][j])
            print(unmarked, n)
            print(unmarked * int(n))
            break
