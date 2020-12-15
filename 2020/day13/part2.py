from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

earliest = int(l[0])
busStr = l[1]

need = []
for i, b in enumerate(busStr.split(',')):
    if b == 'x':
        continue
    need.append((int(b), i))

# kill me
def inv(a, m) : 
    m0 = m 
    x0 = 0
    x1 = 1

    if (m == 1) : 
            return 0

    # apply extended Euclid Algorithm 
    while (a > 1) : 
            q = a // m 

            t = m 

            # m is remainder now, process 
            # same as euclid's algo 
            m = a % m 
            a = t 

            t = x0 

            x0 = x1 - q * x0 

            x1 = t 
    
    if (x1 < 0) : 
            x1 = x1 + m0 

    return x1 

def findMinX(num, rem, k) : 
    prod = 1
    for i in range(0, k) : 
            prod = prod * num[i] 

    result = 0

    # apply above formula 
    for i in range(0,k): 
            pp = prod // num[i] 
            result = result + rem[i] * inv(pp, num[i]) * pp 
   
    # GFY
    return result % prod 

print(findMinX([el[0] for el in need], [-el[1] for el in need], len(need)))
