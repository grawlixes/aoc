# O(N)

l = list(open("./input.txt", 'r').readlines())

j = 0
ret = 0
for line in l:
    line = line.strip()
    ret += line[j] == '#'
    j = (j + 3) % len(line)

print(ret)
