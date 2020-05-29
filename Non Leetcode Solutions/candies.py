t=int(input())
for i in range(t):
    _=input()
    n=int(input())
    l=[]
    for j in range(n):
        x=int(input())
        l.append(x)
    if sum(l)%n==0:
        print("YES")
    else:
        print("NO")
        
