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

    # START CODING HERE
    holding = {}
    weight = {}
    heldBy = {}
    for line in prob:
        name = line[:line.index(' ')]
        w = int(line[line.index('(')+1:\
                     line.index(')')])
        weight[name] = w
        if '->' in line:
            arr = line[line.index('>') + 2:].split(', ')
            holding[name] = set()
            for el in arr:
                heldBy[el] = name
                holding[name].add(el)

    def dfs(name):
        w = weight[name] 
        if name not in holding:
            return w
        
        s = [(dfs(h), h) for h in holding.get(name, set())]
        if len(set([el[0] for el in s])) == 2:
            ct = {}
            m = {}
            for s2, name2 in s:
                ct[s2] = ct.get(s2, 0) + 1
                m[s2] = name2

            k = list(ct.keys())
            badName = None
            good, bad = None, None
            if ct[k[0]] > 1:
                badName = m[k[1]]
                good, bad = k[0], k[1]
            else:
                badName = m[k[0]]
                good, bad = k[1], k[0]

            print(good - bad + weight[badName])

            exit()
        else:
            return w + sum(el[0] for el in s)

    dfs([el for el in weight if el not in heldBy][0])
