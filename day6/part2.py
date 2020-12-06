l = list(el.strip() for el in open("./input.txt", 'r').readlines())

qs = {}
size = 0
ret = 0
for line in l:
    if line == '':
        ret += sum(qs[el] == size for el in qs)
        qs = {}
        size = 0
    else:
        size += 1
        for ch in line:
            qs[ch] = qs.get(ch, 0) + 1

print(ret + sum(qs[el] == size for el in qs))
