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
    temp = prob[0]
    i = 2
    rules = {}
    while i < len(prob):
        r, o = prob[i].split('->')
        rules[r.strip()] = o.strip()
        i += 1

    stack = []
    ct = {}
    for i in range(len(temp) - 1):
        this = temp[i] + temp[i+1]
        ct[this] = ct.get(this, 0) + 1
    
    for i in range(40):
        new = {}
        for el in ct:
            if el not in rules:
                new[el] = new.get(el, 0) + ct[el]
            else:
                out = rules[el]
                f, s = el[0] + out, out + el[1]
                new[f] = new.get(f, 0) + ct[el]
                new[s] = new.get(s, 0) + ct[el]
        ct = new
        #print(ct)
        if i == 2:
            pass
            #break
    ret = {el:0 for el in "abcdefghijklmnopqrstuvwxyz".upper()}
    for dbl in ct:
        ret[dbl[0]] += ct[dbl] // 2
        ret[dbl[1]] += ct[dbl] // 2

    print(max(ret.values()) - min(el for el in ret.values() if el != 0))
