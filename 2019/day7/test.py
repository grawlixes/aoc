x = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5] 
ogx = x[:]
inp = 0
while True:
    #x = ogx[:]
    for phase in [9, 8, 7, 6, 5]:
        cond = False 
        if not cond:
                x[26] = phase - 4
        x[27] = inp * 2 + x[26] 
        inp = x[27]
        x[28] -= 1
        print(inp)
        if x[28] != 0:
                cond = True
        else:
                break
