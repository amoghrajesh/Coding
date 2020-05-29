n=int(input())
j=0
while j<100 and n!=1:
    x=str(n)
    sq=0
    for i in x:
        sq+=int(i)**2
    n=int(sq)
    j+=1
if n==1:
    print(j)
else:
    print(-1)
        
    
    
