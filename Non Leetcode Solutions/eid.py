t=int(input())
for p in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    diff=10**20
    a.sort()
    for i in range(n-1):
        if a[i+1]-a[i]<diff:
            diff=a[i+1]-a[i]
    print(diff)
