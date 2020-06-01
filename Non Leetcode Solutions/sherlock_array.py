n = int(input())
l = list(map(int, input().split()))

left = [l[0]]
for i in range(1,n):
    left.append(left[i-1] + l[i])

li = l[::-1]
right = [li[0]]
for i in range(1,n):
    right.append(right[i-1] + li[i])

right = right[::-1]
found = 0
for i in range(n):
    if left[i] == right[i]:
        found = 1

print(found)
