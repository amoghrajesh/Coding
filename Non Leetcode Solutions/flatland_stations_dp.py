n = int(input())
c = list(map(int, input().split()))

left = [0]*n
right = [0]*n

flagarray = [0]*n
for i in c:
    flagarray[i] = 1

for i in range(len(flagarray)):
    if flagarray[i]==1:
        left[i] = 0
    else:
        if i==0:
            left[i] = 10**9
        else:
            left[i] = left[i-1] + 1

flagarray = flagarray[::-1]
for i in range(len(flagarray)):
    if flagarray[i]==1:
        right[i] = 0
    else:
        if i==0:
            right[i] = 10**9
        else:
            right[i] = right[i-1] + 1

right = right[::-1]

ans = -1
for i in range(n):
    ans = max(ans, min(left[i],right[i]))
print(ans)


