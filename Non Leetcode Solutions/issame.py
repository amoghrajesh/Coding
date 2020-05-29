t=int(input())
def issame(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if(l[i]==l[j]):
                return 1
    return 0
    
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    k=issame(l)
    if(k==1):
        print("Yes")
    else:
        print("No")
    
