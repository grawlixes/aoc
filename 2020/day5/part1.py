l = list(el.strip() for el in open("./input.txt", 'r').readlines())

ret = 0
for el in l:
    first = sum((el[i] == 'B') << (7 - i - 1) for i in range(7))
    second = sum((el[i + 7] == 'R') << (3 - i - 1) for i in range(3))

    ret = max(ret, first * 8 + second) 

print(ret)
