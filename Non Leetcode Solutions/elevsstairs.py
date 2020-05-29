import math
t=int(input())
for i in range(t):
    n,v1,v2=input().split()
    n,v1,v2=int(n),int(v1),int(v2)
    ts=math.sqrt(2) * n /v1
    te=2*n/v2
    if(ts>te):
        print("Elevator")
    else:
        print("Stairs")
