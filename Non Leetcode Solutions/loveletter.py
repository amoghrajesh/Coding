import math
t=int(input())
for i in range(t):
    s=input()
    n=len(s)
    f=math.ceil(n/2)
    
    c=0
    for i in range(f):
       c+=(abs(ord(s[n-1-i])-ord(s[i])))
    print(c)
