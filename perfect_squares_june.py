from math import ceil, sqrt
n = int(input())
dp = [0, 1, 2, 3]
if n<=3:
    print(dp[n])
else:
    for i in range(4, n + 1):
        dp.append(i)
        for x in range(1, ceil(sqrt(i)) + 1):
            temp = x*x
            if temp>i:
                break
            else:
                dp[i] = min(dp[i], 1 + dp[i - temp])
print(dp[-1])