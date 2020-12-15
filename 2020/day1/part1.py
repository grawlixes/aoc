# O(N^2)

nums = list(map(int, open("./input.txt", 'r').readlines()))
print([num1 * num2 for num1 in nums for num2 in nums if num1 + num2 == 2020][0])
