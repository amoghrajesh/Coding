t=int(input())
for k in range(t):
    n,m=input().split()
    n=int(n)
    done=list(map(int,input().split()))
    s=set(range(1,n+1))
    left=s.difference(set(done))
    left=list(sorted(left))
    c=[]
    a=[]
    for j in range(len(left)):
        if j&1==1:
            a.append(left[j])
        else:
            c.append(left[j])
    for i in c:
        print(i,end=' ')
    print()
    for i in a:
        print(i,end=' ')
    print()
