from functools import lru_cache, reduce
from itertools import islice, permutations, combinations
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

    og1 = deque()
    i = 1
    while prob[i] != '':
        og1.append(int(prob[i]))
        i += 1

    og2 = deque()
    i += 2
    while i < len(prob):
        og2.append(int(prob[i]))
        i += 1

    def serialize(p1, p2):
        return (tuple(p1), tuple(p2))

    ma = [0]
    def dfs(p1, p2, game = 1):
        seen = set()
        round = 1
        p1 = p1.copy()
        p2 = p2.copy()
        while p1 and p2:
            this = serialize(p1, p2)
            if this in seen:
                return True, p1
            seen.add(this)

            one, two = p1.popleft(), p2.popleft()

            if one <= len(p1) and \
               two <= len(p2):
                n1 = deque(islice(p1, one), maxlen=one + two)
                n2 = deque(islice(p2, two), maxlen=one + two)
                oneWins, winner = \
                        dfs(n1, \
                            n2, \
                            game + 1)
               
                if oneWins:
                    p1.append(one)
                    p1.append(two)
                else: 
                    p2.append(two)
                    p2.append(one)
        
            else:
                if one > two:
                    p1.append(one)
                    p1.append(two)
                else:
                    p2.append(two)
                    p2.append(one)
            
            round += 1 

        return (len(p1) > 0), (p1 or p2) 
    
    _, w = dfs(og1, og2)
    
    print(sum((el)*(i+1) for i,el in enumerate(reversed(w))))
