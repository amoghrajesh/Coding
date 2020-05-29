t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    for i in range(n):
        s=input()
        l.append(s)
    big="".join(l)
    c=big.count('c')
    o=big.count('o')
    d=big.count('d')
    h=big.count('h')
    e=big.count('e')
    f=big.count('f')
    c1=c//2
    e1=e//2
    ans=min(c1,o,d,e1,h,f)
    print(ans)
    
