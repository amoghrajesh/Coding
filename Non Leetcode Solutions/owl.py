l1=int(input())
r1=int(input())
l2=int(input())
r2=int(input())
k=int(input())
a=set(range(l1,r1+1))
b=set(range(l2,r2+1))
s=a.intersection(b)
s1={k}
s2=s-s1
print(len(s2))
