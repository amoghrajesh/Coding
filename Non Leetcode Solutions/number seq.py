t=int(input())
for i in range(t):
    x,y=list(map(int,input().split()))
    if x==y:
        if x%2==0:
            print(x+y)
        else:
            print(x+y-1)
    elif x-2==y:
        if x%2==0:
            print(x+y)
        else:
            print(x+y-1)
    else:
        print("No Number")
    
    
