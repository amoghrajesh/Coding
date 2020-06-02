from collections import Counter
l = list(map(int,input().split()))
m = len(l)//2
c = Counter(l)
for i in c:
    if c[i] == m:
        print(i)