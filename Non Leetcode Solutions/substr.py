from itertools import permutations
n,m=list(map(int,input().split()))
s=input()
pat=[]
for i in range(m):
    pat.append(input())
perm=permutations(pat)
cent=0
for i in perm:
    l=list(i)
    v=''.join(l)
    if v in s:
        cent+=1
print(cent)
