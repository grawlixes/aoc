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
inp = 1
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
        outp.append(nums[v[0]])
    else:
        print("Error at i = " + str(i) + "; found " + str(nums[i]))
        break

    i += len(params) + 1

print(outp)
