t=int(input())
for i in range(t):
    ap=list(map(int,input().split()))
    s=ap[-1]
    n=(2*s)//(ap[0]+ap[1])
    d=(ap[1]-ap[0])//(n-3 - 2)
    a=ap[0]-(2*d)
    print(n)
    for i in range(n):
        print(a+i*d,end=" ")
