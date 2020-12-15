from functools import lru_cache, reduce
from itertools import permutations, combinations
import math

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

acc = 0
seen = set()
i = 0
while True:
    line = l[i]
    if i in seen:
        print(acc)
        break
    seen.add(i)
    
    op, arg = line.split(' ') 
    if op == "jmp":
        i += int(arg)
    else:
        acc += int(arg) * (op == 'acc')
        i += 1
