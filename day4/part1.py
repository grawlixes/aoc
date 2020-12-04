l = list(el.strip() for el in open("./input.txt", 'r').readlines())

need = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
ogNeed = need.copy()
ret = 0
for line in l:
    if len(line) == 0:
        ret += len(need) == 0
        need = ogNeed.copy()
    else:
        for n in need.copy():
            if n in line:
                need.remove(n)

# I forgot the fucking last entry until like 10 minutes into the problem. I hate coding
print(ret + (len(need) == 0))
