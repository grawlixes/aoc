from functools import lru_cache, reduce
from itertools import permutations, combinations
import math
from collections import deque

mine = list(el.strip() for el in open("./input.txt", 'r').readlines())

# slow but it works lol. give it 20 seconds or so

for prob in [mine]:
    # skips if we didn't find any sample input in our scan
    if not prob:
        continue

    nums = list(map(int, prob[0].split(',')))
    m = {}
    for i in range(30000000):
        if i < len(nums):
            m[nums[i]] = i
        else:
            num = nums[-1]
            if num not in m:
                nums.append(0)
            else:
                nums.append(i - m[num] - 1)
            m[num] = i - 1

    print(nums[30000000 - 1])
