t=int(input())
for i in range(t):
    n=int(input())
    h=list(map(int,input().split()))
    l=0
    r=n-1
    lm,rm=0,0
    ans=0
    while l<r:
        if h[l]<h[r]:
            if h[l]>lm:
                lm=h[l]
            else:
                ans+=(lm-h[l])
            l+=1
        else:
            if h[r]>rm:
                rm=h[r]
            else:
                ans+=(rm-h[r])
            r-=1
        
    print(ans)
