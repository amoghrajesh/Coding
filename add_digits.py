n = int(input())
l = len(str(n))
while l > 1:
    s=0
    for i in str(n):
        s += int(i)
    n = s
    l = len(str(n))
print(n)
