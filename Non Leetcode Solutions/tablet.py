t=int(input())
for i in range(t):
    n,b=input().split()
    n,b=int(n),int(b)
    high=0
    area=0
    for i in range(n):
        w,h,p=input().split()
        w,h,p=int(w),int(h),int(p)
        if(p<=b):
            area=h*w
        if(high<area):
            high=area
    if(area!=0):
        print(high)
    else:
        print("no tablet")
    
        
        
