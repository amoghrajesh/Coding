from math import ceil
n = int(input())
k = int(input())
arr = list(map(int, input().split()))

hashmap = dict()

pagenum = 1
for probs in arr:
    p = ceil(probs/k)
    r = range(1,probs + 1)
    start = 1
    for j in range(pagenum,pagenum + p):
        hashmap[j] = range(start, min(start + k, probs + 1))
        start = start + k
    pagenum += p
ans=0
for i in hashmap:
    if i in hashmap[i]:
        ans+=1
print(ans)