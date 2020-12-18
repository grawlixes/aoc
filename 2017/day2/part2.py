from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

sample = None
mine = list(el.strip() for el in open("./input.txt", 'r').readlines())

for prob in [sample, mine]:
    if not prob or not prob[0]:
        continue

    ret = 0
    for l in prob:
        nums = list(map(int, l.split('\t')))
        nums.sort()

        succ = False
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]

                if num2 % num1 == 0:
                    ret += num2 // num1
                    succ = True
                    break

            if succ:
                break



    print(ret)
