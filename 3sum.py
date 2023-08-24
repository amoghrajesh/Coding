A=list(map(int,input().split()))
target=int(input())
n=len(A)

count=[0]*101
for i in A:
    count[i]+=1
ans=0
#Case 1: when x!=y!=z
for x in range(101-1):
    for y in range(x+1,101):
        z=target-x-y
        if z>y:
            ans+=(count[x]*count[y]*count[z])

#Case 2: when x==y!=z
for x in range(101):
    t=target-(2*x)
    if t%2!=1:
        z=t//2
        if z>x:
            ans+=(count[z]*count[x]*(count[x]-1)//2)

#Case 3: when x!=y==z
for x in range(101):
    z=target-x
    if z%2!=1:
        z=z//2
        if z>x:
            ans+=(count[x]*count[z]*(count[z]-1)//2)

        

    
#Case 4: all same
if target%3==0:
    x=target//3
    if 0<=x<=100:
        ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6
    
return ans%(10**9+7)
            





