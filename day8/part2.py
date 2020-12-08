from functools import lru_cache, reduce
from itertools import permutations, combinations
import math

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

# (i, acc, changed)
dfs = [(0, 0, False)]
# holds (i, changed)
seen = set()

while dfs:
    i, acc, changed = dfs.pop()
    if i == len(l):
        print(acc)
        break
    elif (i, changed) in seen:
        pass 
    else: 
        seen.add((i, changed))
        
        op, arg = l[i].split(' ') 

        # welcome to hell!!
        if op in ["jmp", "nop"]:
            if op == "nop" or not changed:
                dfs.append((i + 1, \
                            acc, \
                            changed or (op == "jmp")))
            if op == "jmp" or not changed:
                dfs.append((i + int(arg), \
                            acc, \
                            changed or (op == "nop")))
        else:
            acc += int(arg)
            dfs.append((i + 1, acc, changed))
