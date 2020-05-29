t=int(input())
n,m=input().split()
n,m=int(n),int(m)
for i in range(t):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=set(a) & set(b)
    print(len(x))
