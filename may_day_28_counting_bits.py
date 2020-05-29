n = int(input())
dp = [0,1,1]
bits_till_here = 2
if n<=2:
    print(dp[:n+1])

else:
    for i in range(3,n+1):
        if bits_till_here*2<=i:
            bits_till_here = 2*bits_till_here

        j = dp[i%bits_till_here] + 1
        dp.append(j)

    print(dp)