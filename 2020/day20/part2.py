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
    grids = {}
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

        grids[thisId] = []
        for i2 in range(1, 9):
            row = []
            for j2 in range(1, 9):
                row.append(prob[i + i2][j2])
            grids[thisId].append(''.join(row))

        i += 11 

    N = int(math.sqrt(len(tiles)))
    grid = [[None for _ in range(N)] for _ in range(N)]

    used = set()
    save = [[]]
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
                toTry.append([this[2], this[1], ""])
            if (matchUp is None or matchUp == this[3]) and \
               (matchLeft is None or matchLeft == this[2]):
                toTry.append([this[1], this[0], "r90"])
            if (matchUp is None or matchUp == this[2]) and \
               (matchLeft is None or matchLeft == this[1]):
                toTry.append([this[0], this[3], "r180"])
            if (matchUp is None or matchUp == this[1]) and \
               (matchLeft is None or matchLeft == this[0]):
                toTry.append([this[3], this[2], "r270"])

            # flip -> vertical, horizontal, diagLeft, diagRight
            if (matchUp is None or matchUp == rb(this[2])) and \
               (matchLeft is None or matchLeft == rb(this[3])):
                toTry.append([rb(this[0]), rb(this[1]), "fv"])
            if (matchUp is None or matchUp == rb(this[0])) and \
               (matchLeft is None or matchLeft == rb(this[1])):
                toTry.append([rb(this[2]), rb(this[3]), "fh"])
            if (matchUp is None or matchUp == rb(this[3])) and \
               (matchLeft is None or matchLeft == rb(this[0])):
                toTry.append([rb(this[1]), rb(this[2]), "fdl"])
            if (matchUp is None or matchUp == rb(this[1])) and \
               (matchLeft is None or matchLeft == rb(this[2])):
                toTry.append([rb(this[3]), rb(this[0]), "fdr"])

            success = False
            for up, left, orient in toTry:
                if min(i, j) == N - 1:
                    success = True
                    grid[-1][-1] = [up, left, tile, orient]
                    save[0] = deepcopy(grid)
                    break
                else:
                    grid[i][j] = [up, left, tile, orient]
                    used.add(tile)

                    if j == N - 1:
                        dfs(i + 1, 0)
                    else:
                        dfs(i, j + 1)
                    used.remove(tile)
                    grid[i][j] = None

            if success:
                return

    dfs(0, 0)
 
    def reorient(grid, orient):
        ret = [[None for _ in grid[0]] for _ in grid]
        if orient == '':
            return grid
        elif orient[0] == 'r':
            mag = int(orient[1:])
            for _ in range(mag // 90):
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        ret[i][j] = grid[-(j+1)][i]
                grid = deepcopy(ret) 
        elif orient == 'fv':
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    ret[i][j] = grid[-(i+1)][j]
        elif orient == 'fh':
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    ret[i][j] = grid[i][-(j+1)] 
        elif orient == 'fdl':
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    ret[i][j] = grid[j][i]
        elif orient == 'fdr':
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    ret[i][j] = grid[-(j+1)][-(i+1)]
        else:
            print("bad orient", orient)
            exit()

        return ret
    
    save = save[0]
    # now "save" has our grid in some random orientation

    sea = [[None for _ in range(8 * N)] for _ in range(8 * N)]
 
    si = 0
    
    for row in save:
        sj = 0
        for _, _, tile, orient in row: 
            g = reorient(grids[tile], orient)
            for seaI in range(8):
                for seaJ in range(8):
                    gij = g[seaI][seaJ]
                    sea[si * 8 + seaI][sj * 8 + seaJ] = gij
                    pass
            sj += 1
        si += 1

    monster = [el.strip('\n') for el in open("monster.txt", 'r').readlines()]
    m = []
    hashes = sum(cell == '#' for row in sea for cell in row)
    for o in ['', 'r90', 'r180', 'r270', 'fh', 'fv', 'fdl', 'fdr']:
        monsters = 0
        thisSea = reorient(sea, o)

        for i in range(len(thisSea) - len(monster) + 1):
            for j in range(len(thisSea[0]) - len(monster[0]) + 1):
                if all(monster[i2][j2] == ' ' or thisSea[i + i2][j + j2] == monster[i2][j2] for i2 in range(len(monster)) for j2 in range(len(monster[0]))):
                    monsters += 1

        m.append(monsters)

    print(hashes - 15*max(m))
