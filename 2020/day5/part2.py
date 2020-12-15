l = list(el.strip() for el in open("./input.txt", 'r').readlines())

ret = 0
seen = set()
for el in l:
    first = sum((el[i] == 'B') << (7 - i - 1) for i in range(7))
    second = sum((el[i + 7] == 'R') << (3 - i - 1) for i in range(3))

    seen.add((el, first * 8 + second))

seen = sorted(seen, key = lambda t: t[1])
for i, t in enumerate(seen):
    if i != len(seen) - 1 and seen[i][1] != seen[i + 1][1] - 1:
        print(seen[i][1] + 1)
