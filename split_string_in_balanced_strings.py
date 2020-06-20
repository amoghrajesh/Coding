s = input()
ans = 0
p = 0
if s[0] == 'R':
    p = 1
else:
    p = -1

for i in range(1, len(s)):

    if s[i] == 'L':
        p -= 1
    else:
        p += 1

    if p == 0:
        ans+=1
print(ans)