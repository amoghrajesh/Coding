t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    x=0
    for j in l:
        x=x^j
    print(x)
