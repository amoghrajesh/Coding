t=int(input())
def find(n):
    s=sum(map(int,str(n)))
    y=10-s%10    
    return 10*n+y


for i in range(t):
    n=int(input())
    x=find(n)
    print(x)
