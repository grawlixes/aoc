# O(N)

nums = list(map(int, open("./input.txt", 'r').readlines()))

print(sum(num // 3 - 2 for num in nums))
