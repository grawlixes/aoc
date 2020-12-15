# im tired of forgetting to update the TC so im not putting it here anymore lol

from itertools import permutations

nums = list(map(int, open("input.txt", 'r').readline().split(',')))
numsTest = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
nums = list(map(int, numsTest.split(',')))

original = nums[:]

numCodes = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}

class Opcode:
    def __init__(self, n):
        self.op = n % 100
        self.params = []
        n //= 100
        for _ in range(numCodes[self.op]):
            self.params.append(n % 10)
            n //= 10

# 5! = 120 permutations
best = 0
for p in permutations([5, 6, 7, 8, 9]):
    outp = []
    inp = 0
    for k,el in enumerate(p):
        nums = original[:]
        i = 0
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
                if el != float('inf'):
                    nums[v[0]] = el
                    el = float('inf')
                else:
                    nums[v[0]] = inp
            elif op == 4:
                outp.append(nums[v[0]])
                inp = nums[v[0]]
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

    #print(outp[-1], p)
    best = max(best, outp[-1])

print(best)
