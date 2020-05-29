t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ma=max(a)
    a[a.index(ma)]=0
    sa=sum(a)
    mb=max(b)
    b[b.index(mb)]=0
    sb=sum(b)
    if(sa>sb):
        print("Bob")
    elif(sb>sa):
        print("Alice")
    else:
        print("Draw")
