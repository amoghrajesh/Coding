l=list(map(int,input().split()))
target=int(input())

n=len(l)
i=n-1
while i>=0 and l[i]>=target:
    i-=1
print(i+1)
