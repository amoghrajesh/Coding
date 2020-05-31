from collections import Counter
arr = list(map(int, input().split()))
n = len(arr)
#5 4 4 2 2 8
#2 2 4 4 5 8
print(n)
c = Counter(arr)
arr = sorted(set(arr))

for i in range(len(arr)-1):
    n -= c[arr[i]]
    print(n)


