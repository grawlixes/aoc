l = list(el.strip() for el in open("./input.txt", 'r').readlines())

qs = set()
ret = 0
for line in l:
    if line == '':
        ret += len(qs)
        qs = set()
    else:
        qs |= set(line)

print(ret + len(qs))
