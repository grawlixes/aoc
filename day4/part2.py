l = list(el.strip() for el in open("./input.txt", 'r').readlines())

need = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
ogNeed = need.copy()
ret = 0

# just fucking kill me
def check(att, line):
    l = line.split(' ')
    for entry in l:
        val = entry[entry.index(':') + 1:]
        if n == "byr":
            if val.isdigit() and \
               int(val) >= 1920 and \
               int(val) <= 2002:
                   return True
        elif n == "iyr":
            if val.isdigit() and \
               int(val) >= 2010 and \
               int(val) <= 2020:
                   return True
        elif n == "eyr":
            if val.isdigit() and \
               int(val) >= 2020 and \
               int(val) <= 2030:
                   return True 
        elif n == "hgt":
            val2 = val[:-2]
            if val[-2:] == "cm" and \
               val2.isdigit() and \
               int(val2) >= 150 and \
               int(val2) <= 193:
                   return True
            if val[-2:] == "in" and \
               val2.isdigit() and \
               int(val2) >= 59 and \
               int(val2) <= 76:
                   return True
        elif n == "hcl":
            chars = map(chr, range(97, 97 + 26))
            nums = map(str, range(10))
            if val[0] == '#' and \
               len(val) == 7 and \
               all(val[i] in chars or \
                   val[i] in nums for i in range(1, 7)):
                   return True
        elif n == "ecl":
            if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return True
        elif n == "pid":
            if val.isdigit() and \
               len(val) == 9:
                   return True

        return False

for line in l:
    if len(line) == 0:
        ret += len(need) == 0
        need = ogNeed.copy()
    else:
        for n in need.copy():
            if n in line and check(n, line):
                need.remove(n)
        
print(ret + (len(need) == 0))
