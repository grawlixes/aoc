from functools import reduce
from itertools import permutations, combinations
import math

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

contains = {}
contained = {}

# forgive me for these atrocious variable names
for line in l:
    contain = line.index("contain")
    first = line[:contain]
    first = first[:line.index(" bags")]
    if first not in contains:
        contains[first] = set()

    second = line[contain + 8:]
    if second[0] != 'n':
        spl = second.split(', ')
        for el in spl:
            num = int(el[:el.index(' ')])
            cont = el[el.index(' ') + 1:\
                      el.index(" bag")]
            if cont not in contained:
                contained[cont] = set()
            contains[first].add((num, cont))
            contained[cont].add(first)

dfs = ["shiny gold"]
seen = set()
while dfs:
    bag = dfs.pop()
    if bag not in seen:
        seen.add(bag)
        for c in contained.get(bag, set()):
            dfs.append(c)

print(len(seen) - 1)
