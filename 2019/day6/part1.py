# O(N)

lines = list(open("input.txt", 'r').readlines())

orbitedBy = {}

for l in lines:
    orbited, orbits = map(lambda s: s.strip(), l.split(')'))

    if orbited not in orbitedBy:
        orbitedBy[orbited] = set()
    orbitedBy[orbited].add(orbits)

ret = 0
dfs = [("COM", 0)]
while dfs:
    cur, indirect = dfs.pop()
    ret += indirect
    
    for orbits in orbitedBy.get(cur, set()):
        dfs.append((orbits, indirect + 1))

print(ret)
