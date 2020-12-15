# O(U - L)

lower = 272091
upper = 815432
ret = 0

def meetsRules(n):
    div = 1
    prev = None

    equal = False
    while n // div:
        cur = (n // div) - (n // (div * 10)) * 10
        if prev is not None and cur > prev:
            return False

        equal |= (cur == prev)
        prev = cur
        div *= 10

    return equal

print(sum(meetsRules(i) for i in range(lower, upper + 1)))
