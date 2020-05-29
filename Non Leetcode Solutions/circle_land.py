import math
t=int(input())
def near(x):
    k=math.floor(math.sqrt(x))
    return k**2
    
for i in range(t):
    n=int(input())
    c=0
    while(n>0):
        c+=1
        a=near(n)
        print("a:",a)
        n-=a
    print(c)
    
