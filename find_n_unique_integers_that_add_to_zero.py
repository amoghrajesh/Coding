n = int(input())
if n == 1:
    print([0])
else:
    temp = list(range(-n, n+1))
    i = 0
    ans = []
    while n>1:
        ans.insert(0, temp[i])
        ans.insert(len(ans)//2, temp[(-(i+1))])
        i+=1
        n-=2
    x = len(ans)//2
    if n%2==1:
        ans.insert(x, 0)
    print(ans)


