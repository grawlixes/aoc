# O(N)

nums = list(map(int, open("input.txt", 'r').readline().split(',')))
nums[1] = 12
nums[2] = 2

for i in range(0, len(nums), 4):
    if nums[i] == 99:
        break
    elif nums[i] == 1:
        v1 = nums[i + 1]
        v2 = nums[i + 2]
        loc = nums[i + 3]
        nums[loc] = nums[v1] + nums[v2]
    elif nums[i] == 2:
        v1 = nums[i + 1]
        v2 = nums[i + 2]
        loc = nums[i + 3]
        nums[loc] = nums[v1] * nums[v2]
    else:
        print("Error at i = " + str(i) + "; found " + str(nums[i]))
        break

print(nums[0])
