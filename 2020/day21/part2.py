from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque
from copy import deepcopy

sample = None
try:
    #sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
    pass
except:
    pass

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue

    allergens = {}
    ingredients = {}
    occ = {}
    for line in prob:
        ing = set(line[:line.index('(') - 1].split(' '))
        allerg = set(line[line.index("contains") + len("contains") + 1:-1].split(', '))
       
        for i in ing:
            occ[i] = occ.get(i, 0) + 1
            if i not in ingredients:
                ingredients[i] = set() 
        
        for a in allerg:
            if a in allergens:
                allergens[a] &= ing
            else:
                allergens[a] = ing.copy()

    has = {}
    while len(allergens) > 0:
        ra = set()
        ri = set()
        for a in allergens:
            if len(allergens[a]) == 1:
                has[a] = allergens[a].pop()
                ra.add(a)
                ri.add(has[a])

        for a in allergens:
            allergens[a] -= ri
        for a in ra:
            del allergens[a]
    
    print(','.join(has[i] for i in sorted(has.keys())))
