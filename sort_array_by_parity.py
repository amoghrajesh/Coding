l = list(map(int, input().split()))
even = []
odd = []
for i in range(len(l)-1, -1, -1):
    if l[i] % 2 == 0:
        even.append(l[i])
    else:
        odd.append(l[i])
ans = []
while odd and even:
    e = even.pop()
    ans.append(e)
    o = odd.pop()
    ans.append(o)
print(ans)