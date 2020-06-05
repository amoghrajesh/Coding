n = int(input())
rot = {'2':'5', '5':'2', '6':'9', '9':'6'}
# for first 10 elements
dp = [0,0,1,1,1,2,3,3,3,4,4]
if n<=10:
    print(dp[n])
else:
    b = 0
    for i in range(10,n+1):
        b = 0
        for j in str(i):
            if j in rot:
                b = 1
        if b == 1:
            dp.append(dp[-1]+1)
        else:
            dp.append(dp[-1])
    print(dp,len(dp))
