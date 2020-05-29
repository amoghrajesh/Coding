t=int(input())
for i in range(t):
    n,x=input().split()
    n,x=int(n),int(x)
    s=input()
    l=[]
    l.append(x)
    for i in s:
        if(i=='R'):
            x+=1               
            l.append(x)
        else:
            x-=1
            l.append(x)
    print(set(l))
            
    
