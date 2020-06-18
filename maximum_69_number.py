n = int(input())
s = list(str(n))
m = n

for i in range(len(s)):
    if s[i] == '6':
        s[i] = '9'
    else:
        s[i] = '6'
    if int(''.join(s))>m:
        m = int(''.join(s))
    s = list(str(n))
print(m)
