# O(N * lg(el))

nums = list(map(int, open("input.txt", 'r').readlines()))

ret = 0
for num in nums:
    while num > 0:
        num = (num // 3) - 2
        ret += max(num, 0)

print(ret)
