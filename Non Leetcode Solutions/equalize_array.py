from collections import Counter
arr = list(map(int,input().split()))
c = Counter(arr)
m = max(c.values())
print(len(arr) - m)
