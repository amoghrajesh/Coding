arr = list(map(int, input().split()))
d = int(input())
ans = 0
for i in range(len(arr)):
    if arr[i] + d in arr[i+1:] and arr[i]+2*d in arr[i+1:]:
        ans+=1
print(ans)


