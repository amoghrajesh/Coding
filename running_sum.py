l = list(map(int,input().split()))
ans = [l[0]]
for i in range(1, len(l)):
    ans.append(ans[-1] + l[i])
print(ans)
