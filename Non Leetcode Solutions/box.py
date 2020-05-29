n=int(input())
l=list(map(int,input().split()))
l.sort()
i=0
j=0
box=0
while i<n:
    j=i
    while j<n and l[j]<=l[i]+4:
        j+=1
    if j>i:
        box+=1
        i=j
    else:
        break
print(box)
    
    
