t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    for j in range(n):
        if j==0:
            time=a[0]
        else:
            time=a[j]-a[j-1]
        #print(time)
        if b[j]<=time:
            c+=1
    print(c)
    
        
