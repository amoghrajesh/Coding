t=int(input())
for i in range(t):
    b,w=list(map(int,input().split()))
    bc,wc,z=list(map(int,input().split()))
    if bc<wc:
        if bc+z<wc:
            cost=bc*b+(bc+z)*w
        else:
            cost=bc*b+wc*w
    elif bc==wc:
        cost=bc*b+wc*w
    else:
        if wc+z<bc:
            cost=(wc+z)*b+wc*w
        else:
            cost=bc*b+wc*w
    print(cost)
        
