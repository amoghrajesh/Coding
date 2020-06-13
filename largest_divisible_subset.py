l = list(map(int, input().split()))
n = len(l)
if n == 0:
    print([])
l.sort()
dp = [1 for i in range(n)]
prev = [-1 for i in range(n)]
last_index = 0
for i in range(0, n):
    for j in range(i):
        if l[i] % l[j] == 0:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    if dp[last_index]<dp[i]:
        last_index = i
i = last_index
res = []
while i>=0:
    res.append(l[i])
    i = prev[i]
print(sorted(res))

