# O(N^2)

nums = list(map(int, open("input.txt", 'r').readlines()))

dp = {nums[i]: i for i in range(len(nums))}

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        comp = 2020 - (nums[i] + nums[j])
        if dp.get(comp, -1) not in [-1, i, j]:
            print(nums[i] * nums[j] * comp)
            exit()
