t=int(input())
def f(n):
    c=0
    num=19
    while c!=n:
        num+=9
        s=sum(map(int,str(num)))
        if s%10==0:
            c+=1
    return num-9
for i in range(t):
    n=int(input())
    print(f(n))
