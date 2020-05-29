from math import sqrt
def fib(n):
    f=((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n
    f=f/sqrt(5)
    return int(f)

n=4000000
m=3
ans=[]
'''for i in range(1,n):
    ans.append(fib(int(i)))'''
for i in range(2,n+2):
    f=fib(i)
    if f>4000000:
        break
    else:
        ans.append(f)

s=sum([x for x in ans if x%2==0])
print(s)
