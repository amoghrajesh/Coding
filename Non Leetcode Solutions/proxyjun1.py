import math

def proxy(l,b):
    x=0
    for i in range(2,len(l)-2):
        if(l[i]=='A' and b>0):
            if((l[i-1]=='P' or l[i-2]=='P') and (l[i+1]=='P' or l[i+2]=='P')):
                b-=1
                x+=1
        if b==0:
            return x
    return -1
            

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=list(s)
    x=math.ceil(n*0.75)
    b=x-l.count('P')
    print(proxy(l,b))
