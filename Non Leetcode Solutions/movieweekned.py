t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    z=list(zip(l,r))
    m=max(list(map(lambda x:x[0]*x[1],z)))
    rs=[]
    for j in range(len(z)):
        if z[j][0]*z[j][1]==m:
            beg=j
            bigr=z[j][1]
            break
    temp=beg+1
    g=0
    for j in range(beg+1,len(z)):
        if z[j][0]*z[j][1]==m:
            if z[j][1]>bigr:
                beg=j
                bigr=z[j][1]
            elif bigr==z[j][1]:
                g=1
                print(temp+1)
                break
    if g==0:
        #print("yaha")
        print(beg+1)
    
        
        
