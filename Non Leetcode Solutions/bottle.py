t=int(input())
for i in range(t):
    x1,x2,x3,v1,v2=input().split()
    x1,x2,x3,v1,v2=int(x1),int(x2),int(x3),int(v1),int(v2)
    dchef=abs(x3-x1)
    dkefa=abs(x3-x2)
    tchef=dchef/v1
    tkefa=dkefa/v2
    if(tchef>tkefa):
        print("Kefa")
    elif(tchef<tkefa):
        print("Chef")
    else:
        print("Draw")
