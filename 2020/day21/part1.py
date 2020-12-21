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

    bad = set(i for a in allergens for i in allergens[a])

    print(sum(occ[i] for i in occ if i not in bad))

