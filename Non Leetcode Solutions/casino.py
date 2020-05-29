t=int(input())
for i in range(t):
    n,a,b=input().split()
    n,a,b=int(n),int(a),int(b)
    x=list(map(int,input().split()))
    pa=(x.count(a)/n)
    pb=(x.count(b)/n)
    ans=pa*pb
    print('{0:.10f}'.format(ans))
