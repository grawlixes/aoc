# O(N^2)

l = list(open("./input.txt", 'r').readlines())

ret = 0
for line in l:
    s = line.split(' ')
    mi, ma = list(map(int, s[0].split('-')))
    ch = s[1][0]
    st = s[2].strip()

    ret += (st[mi - 1] == ch) ^ (st[ma - 1] == ch) 

print(ret)
