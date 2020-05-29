n=int(input())
th=list(range(1,n+1))
l=list(map(int,input().split()))
s=set(l)
for i in s:
    if i!=0:
        th.remove(i)
for i in th:
    print(i,end=" ")
