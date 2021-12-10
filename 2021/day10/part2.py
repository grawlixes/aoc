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
    comp = {'(':')', '{':'}', '[':']', '<':'>'}
    score = {')': 1, ']': 2, '}': 3, '>': 4}    
    ret = 0
    s = []
    for line in prob:
        stack = []
        good = True
        for ch in line:
            if ch in ")}]>":
                if not stack or ch != comp[stack[-1]]:
                    good = False
                    break
                stack.pop()
            else:
                stack.append(ch)

        if good:
            sc = 0
            while stack:
                sc = 5 * sc + score[comp[stack.pop()]]
            s.append(sc)

    s.sort()
    print(s[len(s)//2])
