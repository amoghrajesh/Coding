t=int(input())
for i in range(t):
    n,k=input().split()
    n,k=int(n),int(k)
    l=list(map(int,input().split()))
    l.sort()
    print(l[(n+k)//2])
