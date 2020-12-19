from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque
from copy import deepcopy

sample = None
try:
#    sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
    pass
except:
    pass

personal = list(el.strip() for el in open("./input.txt", 'r').readlines())
for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue

    rules = {}
    i = 0
    while len(prob[i]):
        line = prob[i]
        first = int(line[:line.find(':')])
        second = line[line.find(':') + 2:]
        if '"' in second:
            rules[first] = second.strip('"')
        else:
            line = second
            rules[first] = []
            while '|' in line:
                ind = line.find('|')
                rules[first].append(list(map(int, line[:ind-1].split(' '))))
                line = line[ind + 2:]
            rules[first].append(list(map(int, line.split(' '))))
        i += 1

    @lru_cache(None)
    def dfs(s, r):
        if type(rules[r]) == str:
            return rules[r] == s
        else:
            for lst in rules[r]:
                if len(lst) == 1:
                    if dfs(s, lst[0]):
                        return True
                else:
                    for i in range(len(s)):
                        if dfs(s[:i+1], lst[0]) and \
                           dfs(s[i+1:], lst[1]):
                               return True
            
            return False
    
    i += 1
    ret = 0
    while i < len(prob):
        ret += dfs(prob[i], 0)
        i += 1
    print(ret)
    break
