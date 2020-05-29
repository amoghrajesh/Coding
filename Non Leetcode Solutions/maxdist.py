from math import sqrt
t=int(input())
pts=[]
xs=[]
ys=[]
for i in range(t):
    x,y=input().split()
    x,y=int(x),int(y)
    xs.append(x)
    ys.append(y)

minx,maxx=min(xs),max(xs)
miny,maxy=min(ys),max(ys)
d1=abs(minx-maxx)
d2=abs(miny-maxy)
d3=sqrt(minx**2+maxy**2)
d4=sqrt(miny**2+maxx**2)
d5=sqrt(maxx**2+maxy**2)
d6=sqrt(minx**2+miny**2)
print("{0:.6f}".format(max(d1,d2,d3,d4,d5,d6)))


        

    
