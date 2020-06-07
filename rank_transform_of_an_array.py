l = list(map(int,input().split()))
arr = sorted(l)
c = 1
hashmap = dict()

for i in arr:
    if i not in hashmap:
        hashmap[i] = c
        c+=1

ans = []
for i in l:
    ans.append(hashmap[i])

print(ans)