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

    def rb(n):
        return sum(((n >> i) & 1) << (10 - i - 1) for i in range(10))

    i = 0
    tiles = {}
    while i < len(prob):
        thisId = int(prob[i][prob[i].index(' ') + 1:-1])
        i += 1

        tiles[thisId] = []
        # up
        tiles[thisId].append(sum((prob[i][j] == '#') << j for j in range(10)))
        # right
        tiles[thisId].append(sum((prob[i+j][-1] == '#') << j for j in range(10)))
        # down
        tiles[thisId].append(sum((prob[i+9][j] == '#') << (10 - 1 - j) for j in range(10)))
        # left
        tiles[thisId].append(sum((prob[i+j][0] == '#') << (10 - 1 - j) for j in range(10)))

        i += 11 

    N = int(math.sqrt(len(tiles)))
    grid = [[None for _ in range(N)] for _ in range(N)]

    used = set()
    def dfs(i, j):
        for tile in tiles:
            if tile in used:
                continue
            
            matchUp = None if i == 0 else grid[i-1][j][0]
            matchLeft = None if j == 0 else grid[i][j-1][1]

            if matchUp is not None:
                matchUp = rb(matchUp)
            if matchLeft is not None:
                matchLeft = rb(matchLeft)

            this = tiles[tile]
            toTry = []
            # rotate -> 0, 90, 180, 270
            if (matchUp is None or matchUp == this[0]) and \
               (matchLeft is None or matchLeft == this[3]):
                toTry.append([this[2], this[1]])
            if (matchUp is None or matchUp == this[3]) and \
               (matchLeft is None or matchLeft == this[2]):
                toTry.append([this[1], this[0]])
            if (matchUp is None or matchUp == this[2]) and \
               (matchLeft is None or matchLeft == this[1]):
                toTry.append([this[0], this[3]])
            if (matchUp is None or matchUp == this[1]) and \
               (matchLeft is None or matchLeft == this[0]):
                toTry.append([this[3], this[2]])

            # flip -> vertical, horizontal, diagLeft, diagRight
            if (matchUp is None or matchUp == rb(this[2])) and \
               (matchLeft is None or matchLeft == rb(this[3])):
                toTry.append([rb(this[0]), rb(this[1])])
            if (matchUp is None or matchUp == rb(this[0])) and \
               (matchLeft is None or matchLeft == rb(this[1])):
                toTry.append([rb(this[2]), rb(this[3])])
            if (matchUp is None or matchUp == rb(this[3])) and \
               (matchLeft is None or matchLeft == rb(this[0])):
                toTry.append([rb(this[1]), rb(this[2])])
            if (matchUp is None or matchUp == rb(this[1])) and \
               (matchLeft is None or matchLeft == rb(this[2])):
                toTry.append([rb(this[3]), rb(this[0])])


            for up, left in toTry:
                if min(i, j) == N - 1:
                    print(grid[0][0][2] * \
                          grid[0][-1][2] * \
                          grid[-1][0][2] * \
                          tile)
                    exit()
                else:
                    grid[i][j] = [up, left, tile]
                    used.add(tile)

                    if j == N - 1:
                        dfs(i + 1, 0)
                    else:
                        dfs(i, j + 1)
                    used.remove(tile)
                    grid[i][j] = None
    dfs(0, 0)
