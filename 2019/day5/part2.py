# O(N)

nums = list(map(int, open("input.txt", 'r').readline().split(',')))

numCodes = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}

class Opcode:
    def __init__(self, n):
        self.op = n % 100
        self.params = []
        n //= 100
        for _ in range(numCodes[self.op]):
            self.params.append(n % 10)
            n //= 10

i = 0
inp = 5 
outp = []
while True:
    opcode = Opcode(nums[i])
    op = opcode.op
    params = opcode.params

    v = [i + j + 1 if params[j] else nums[i + j + 1] for j in range(len(params))]
    if op == 99:
        break
    elif op == 1:
        nums[v[2]] = nums[v[0]] + nums[v[1]]
    elif op == 2:
        nums[v[2]] = nums[v[0]] * nums[v[1]]
    elif op == 3:
        nums[v[0]] = inp
    elif op == 4:
        print(nums[v[0]])
        break
    elif op == 5:
        if nums[v[0]]:
            i = nums[v[1]]
            i -= len(params) + 1
    elif op == 6:
        if nums[v[0]] == 0:
            i = nums[v[1]]
            i -= len(params) + 1
    elif op == 7:
        nums[v[2]] = 1 if nums[v[0]] < nums[v[1]] else 0
    elif op == 8:
        nums[v[2]] = 1 if nums[v[0]] == nums[v[1]] else 0
    else:
        print("Error at i = " + str(i) + "; found " + str(nums[i]))
        break

    i += len(params) + 1
