price=list((map(int,input().split())))
n = len(price)
ans = [0] * (n)
lastIndex = n - 1
i = lastIndex
while i >= 0:
    temp = 0
    j = i
    while j >= 0 and price[j] <= price[i]:
        temp += 1
        j -= 1

    ans[i] = temp

    i -= 1
print(ans)
