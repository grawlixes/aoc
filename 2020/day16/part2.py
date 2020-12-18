from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

sample = None
#sample = list(el.strip() for el in open("./sampleInput.txt", 'r').readlines())
personal = list(el.strip() for el in open("./input.txt", 'r').readlines())

for prob in [sample, personal]:
    # skips if we didn't find any sample input in our scan
    if not prob or not prob[0]:
        continue

    # START CODING HERE
    i = 0
    m = {}
    while len(prob[i]):
        l = prob[i]
        f = l[:l.index(':')]
        t = [[-1, -1], [-1, -1]]
        l = l[l.index(':')+2:]
        t[0][0] = int(l[:l.index('-')])
        l = l[l.index('-')+1:]
        t[0][1] = int(l[:l.index(' ')])
        l = l[l.index(' ')+4:]

        t[1][0] = int(l[:l.index('-')])
        l = l[l.index('-')+1:]
        t[1][1] = int(l)

        m[f] = t
        i += 1

    while prob[i] != "your ticket:":
        i += 1
    i += 1
    mine = list(map(int, prob[i].split(',')))

    while prob[i] != "nearby tickets:":
        i += 1
    i += 1

    ret = 0
    good = []
    for j in range(i, len(prob)):
        failed = False
        for num in map(int, prob[j].split(',')):
            fail = True 
            for f in m:
                if (num >= m[f][0][0] and num <= m[f][0][1]) or \
                    (num >= m[f][1][0] and num <= m[f][1][1]):
                       fail = False
                       break
            ret += fail * num
            if fail:
                failed = True
                break
        if not failed:
            good.append(list(map(int, prob[j].split(','))))
    
    fields = {}
    done = set()
    while len(fields) != len(good[0]):
        for j in range(len(good[0])):
            if j in done:
                continue
            gotten = [] 
            for el in list(m.keys()):
                bad = False
                for i in range(len(good)):
                    num = good[i][j]
                    if (num not in range(m[el][0][0], m[el][0][1] + 1)) and \
                       (num not in range(m[el][1][0], m[el][1][1] + 1)):
                            bad = True
                            break
                if not bad:
                    gotten.append(el)

            if len(gotten) == 1:
                fields[gotten[0]] = j
                done.add(j)
                del m[gotten[0]]
                break

    ret = 1
    for f in fields:
        if f[:len("departure")] == "departure":
            ret *= mine[fields[f]]
    print(ret)
    #break
