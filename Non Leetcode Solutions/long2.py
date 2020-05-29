def nth(n):
    c=0
    l=[]
    for i in range(19,pow(2,64)+1,9):
        s=sum(map(int,str(i)))
        if(s%10==0):
            l.append(i)
    return l
            

        
t=int(input())
for i in range(t):
    n=int(input())
    x=nth(n)
    print(x)
