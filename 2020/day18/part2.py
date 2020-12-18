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
        newS = []
        while k < len(s):
            if s[k] == '(':
                res = dfs(s, k + 1)
                if op is None:
                    ret = res
                elif op == 2:
                    newS.append(ret)
                    ret = res
                else:
                    ret += res
                k += 1
                d = 1
                while d:
                    d += s[k] == '('
                    d -= s[k] == ')'
                    k += 1
                k -= 1
            elif s[k] == ')':
                break
            elif s[k].isdigit():
                cur = (cur * 10) + int(s[k])

                if k == len(s) - 1 or not s[k+1].isdigit():
                    if op == 0:
                        ret += cur
                    elif op == 2:
                        newS.append(ret)
                        ret = cur
                    else:
                        ret = cur
                    cur = 0
            else:
                op = indMap[s[k]]
            k += 1
      
        newS.append(ret)
        return reduce(lambda x,y: x*y, newS)

    ret = 0
    for line in prob:
        line = ''.join(el for el in line if el != ' ')
        this = dfs(line, 0)
        ret += this

    print(ret)
