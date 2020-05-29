from collections import Counter
s=input()
p=input()
P=Counter(p)
lens=len(s)
lenp=len(p)
ans=[]
for i in range(lens-lenp+1):
    c=Counter(s[i:i+lenp])
    if c==P:
        ans.append(i)
print(ans)


