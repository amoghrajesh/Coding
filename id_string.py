s = input()
n = len(s)
ans = []
lo = 0
hi = n
if s[0]=='I':
    ans.append(lo)
    lo += 1
else:
    ans.append(hi)
    hi -= 1

for i in range(1,n):
    if s[i] == 'I':
        ans.append(lo)
        lo+=1
    else:
        ans.append(hi)
        hi-=1
ans.append(hi)
print(ans)