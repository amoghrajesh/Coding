t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    s=set(l)
    if(len(s)==1):
        print("no")
    else:
        m=max(l)
        l.remove(m)
        if(m==sum(l)):
            print("yes")
        else:
            print("no")
