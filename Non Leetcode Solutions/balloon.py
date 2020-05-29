t=int(input())
for i in range(t):
    s=input()
    l=list(s)
    a=l.count('a')
    b=l.count('b')
    if(a==0 or b==0):
        print(0)
    else:
        print(min(a,b))
