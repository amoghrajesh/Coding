t=int(input())
for i in range(t):
    d1=list(input().split())
    d2=list(input().split())
    sim=0
    for i in d1:
        if i in d2:
            sim+=1
    if(sim>=2):
        print("similar")
    else:
        print("dissimilar")
