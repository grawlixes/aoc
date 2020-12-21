from functools import lru_cache, reduce
from itertools import permutations, combinations
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

    cups = prob[0]
    class Node:
        def __init__(self, x):
            self.val = x
            self.next = None
            self.prev = None

    head = Node(int(cups[0]))
    m = {}
    ptr = head
    head.next = ptr
    m[head.val] = head
    ptr.prev = head
    for i in range(1, len(cups)):
        ptr.next = Node(int(cups[i]))
        ptr.next.prev = ptr
        ptr = ptr.next
        m[ptr.val] = ptr

    for j in range(len(cups) + 1, 1000000 + 1):
        ptr.next = Node(j)
        ptr.next.prev = ptr
        ptr = ptr.next
        m[ptr.val] = ptr

    ptr.next = head
    head.prev = ptr
    ptr = head
    for i in range(10000000):
        three = ptr.next
        three.prev = None
        
        ptr.next = three.next.next.next
        ptr.next.prev = ptr
        three.next.next.next = None
        for it in range(1, 4 + 1):
            nxtI = ptr.val - it
            if nxtI <= 0:
                nxtI = 1000000 + nxtI
            nxt = m[nxtI]
            ptr2 = three
            succ = True
            while ptr2:
                if ptr2 == nxt:
                    nxt = ptr.next
                    succ = False
                    break
                ptr2 = ptr2.next

            if succ:
                break

        tmp = nxt.next
        nxt.next = three
        three.prev = nxt

        three.next.next.next = tmp
        tmp.prev = three.next.next
        ptr = ptr.next

    first = m[1].next
    second = first.next
    print(first.val * second.val)
