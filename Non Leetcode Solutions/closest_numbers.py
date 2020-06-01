n = int(input())
l = list(map(int, input().split()))

l.sort()
m = 10**9
for i in range(n-1):
    if l[i+1]-l[i] < m:
        m = l[i+1]-l[i]
ans = []
for i in range(n-1):
    if l[i+1] - l[i] ==m:
        ans.append(l[i])
        ans.append(l[i+1])

print(ans)

