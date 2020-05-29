t=int(input())
for i in range(t):
    l=[]
    n=int(input())
    s=input()
    print(s)
    x=s.split()
    l.append(x[0])
    for j in range(1,n):
        s=input()
        x=s.split()
        k=x[0]
        if k not in l:
            print(k)
            l.append(k)
        else:
            print(s)
