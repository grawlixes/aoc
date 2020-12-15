# O(N)

lines = list(open("input.txt", 'r').readlines())

orbitMap = {}
cur = None
target = None
for l in lines:
    orbited, orbits = map(lambda s: s.strip(), l.split(')'))

    if orbited not in orbitMap:
        orbitMap[orbited] = set()
    if orbits not in orbitMap:
        orbitMap[orbits] = set()

    if orbits == "YOU":
        cur = orbited
    elif orbits == "SAN":
        target = orbited
    else:
        orbitMap[orbited].add(orbits)
        orbitMap[orbits].add(orbited)

from collections import deque
# (current planet, previous planet, total transfers)
bfs = deque([(cur, None, 0)])
while bfs:
    cur, prev, transfers = bfs.popleft()
    if cur == target:
        print(transfers)
        break

    for o in orbitMap[cur]:
        if o != prev:
            bfs.append((o, cur, transfers + 1))
