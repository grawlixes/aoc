# O(U - L)

lower = 272091
upper = 815432
ret = 0

def meetsRules(n):
    div = 1
    prev = None

    equal = False
    equals = 0 
    while n // div:
        cur = (n // div) - (n // (div * 10)) * 10
        if prev is not None and cur > prev:
            return False

        if cur == prev:
            equals += 1
        else:
            equal |= (equals == 1)
            equals = 0
       
        prev = cur
        div *= 10

    return equal or equals == 1

print(sum(meetsRules(i) for i in range(lower, upper + 1)))
