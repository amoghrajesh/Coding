from collections import Counter
arr = list(map(int, input().split()))
c = Counter(arr)
ans = -1
for i in c:
    if i>ans and c[i] == i:
        ans = i

print(ans)