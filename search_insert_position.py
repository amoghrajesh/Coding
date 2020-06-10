a = list(map(int, input().split()))
target = int(input())
if target<a[0]:
    print(0)
if target>a[-1]:
    print(len(a))
l = 0
r = len(a) - 1
while l<r:
    m = l + (r-l)//2
    if a[m]>=target:
        r = m
    else:
        l = m + 1
print(l)
