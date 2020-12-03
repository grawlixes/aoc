# O(N)

l = list(el.strip() for el in open("./input.txt", 'r').readlines())

rows = len(l)
cols = len(l[0])

tot = 1
for addi, addj in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    i, j = 0, 0
    ret = 0
    while i < rows:
        ret += l[i][j] == '#'
        j = (j + addj) % cols
        i += addi 
    tot *= ret

print(tot)
