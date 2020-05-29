t=int(input())
xzero=[]
yzero=[]
for i in range(t):
    x,y=input().split()
    x,y=int(x),int(y)
    if x==0:
        yzero.append(y)
    else:
        xzero.append(x)

yex=abs(min(xzero)-max(xzero))
why=abs(min(yzero)-max(yzero))
print("{0:.6f}".format(max(yex,why)))
    
