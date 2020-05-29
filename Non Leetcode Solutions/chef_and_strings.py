t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    s0=s.count('0')
    s1=s.count('1')
    r=input()
    r0=r.count('0')
    r1=r.count('1')
    if s0==r0 and s1==r1:
        print("YES")
    else:
        print("NO")
