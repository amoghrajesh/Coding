s = input()
onedict = dict()
onedict[0] = s[1:].count('1')

for i in range(1,len(s)-1):
    if s[i] == '1':
        onedict[i] = onedict[i-1]-1
    else:
        onedict[i] = onedict[i-1]
print(onedict)
ans = 0
zerocount = 0
onecount = 0
m = -1
for i in range(len(s)-1):
    if s[i] == '0':
        zerocount += 1
    onecount = onedict[i]
    m = max(m, zerocount + onecount)

print(m)