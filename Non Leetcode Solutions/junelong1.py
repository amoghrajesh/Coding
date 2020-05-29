import math
def prog(l,left):
    bef=0
    aft=0
    x=0
    for i in range(2,len(l)-2):
        aft=0
        bef=0
        if(l[i]=='A' and (l[i-1]=='P' or l[i-2]=='P')):
            bef=1
            if(l[i+1]=='P' or l[i+2]=='P'):
                aft=1
        p=bef*aft
        if(p==1):
            left-=1
            x+=1
            if(left==0):
                return x
    return -1
            
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=list(s)
    x=math.ceil(n*0.75)
    left=x-l.count('P')
    print(prog(l,left))
