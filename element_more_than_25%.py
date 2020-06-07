from collections import Counter
from math import ceil
l = list(map(int, input().split()))
c = Counter(l)
n = len(l)
x = ceil(0.25*n)
for i in c:
    if c[i]>=x:
        print(i)