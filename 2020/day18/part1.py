from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque
from copy import deepcopy

sample = None
try:
    sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
except:
    pass

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue

    ops = [lambda x,y: x + y,\
           lambda x,y: x - y,\
           lambda x,y: x * y,\
           lambda x,y: x / y]
    indMap = {'+': 0, \
              '-': 1, \
              '*': 2, \
              '/': 3}

    def dfs(s, i):
        cur = 0
        ret = 0
        op = None
        k = i
        while k < len(s):
            if s[k] == '(':
                res, k = dfs(s, k + 1)
                if op is None:
                    ret = res
                else:
                    ret = ops[op](ret, res)
            elif s[k] == ')':
                return (ret, k)
            elif s[k].isdigit():
                cur = (cur * 10) + int(s[k])

                if k == len(s) - 1 or not s[k+1].isdigit():
                    if op is not None:
                        ret = ops[op](ret, cur)
                    else:
                        ret = cur
                    cur = 0
            else:
                op = indMap[s[k]]
            k += 1
        
        return (ret, len(s) - 1)

    ret = 0
    for line in prob:
        line = ''.join(el for el in line if el != ' ')
        this = dfs(line, 0)[0]
        ret += this

    print(ret)
