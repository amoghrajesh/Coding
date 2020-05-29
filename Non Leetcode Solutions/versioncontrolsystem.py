t=int(input())
for i in range(t):
    n,m,k=list(map(int,input().split()))
    tot=set(range(1,n+1))
    ign=list(map(int,input().split()))
    track=list(map(int,input().split()))
    ign=set(ign)
    track=set(track)
    unign=tot-ign
    untrack=tot-track
    print(len(ign.intersection(track)),len(unign.intersection(untrack)))
