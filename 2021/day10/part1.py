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
    score = {')': 3, ']': 57, '}': 1197, '>': 25137}    
    ret = 0
    for line in prob:
        stack = []
        for ch in line:
            if ch in ")}]>":
                if not stack or ch != comp[stack[-1]]:
                    ret += score[ch]
                    break
                stack.pop()
            else:
                stack.append(ch)

    print(ret)
