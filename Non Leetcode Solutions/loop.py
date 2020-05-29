t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    A,B=[],[]
    for j in range(m):
        u,v=list(map(int,input().split()))
        A.append(u)
        B.append(v)
    if len(A)==1 and len(B)==1:
        print("safe")
    elif len(set(A))<=len(set(B)):
        print("unsafe")
    else:
        print("safe")
