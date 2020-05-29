t=int(input())
for i in range(t):
    a,b=list(map(int,input().split()))
    l=1
    bob=2
    while 1:
        a-=l
        l+=2
        if a<0:
            print("Bob")
            break
        b-=bob
        bob+=2
        if b<0:
            print("Limak")
            break
