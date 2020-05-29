# Write your code here
n=int(input())
l=list(map(int,input().split()))
c=0

for i in range(n):
    if l[i]!=0:
        l[c]=l[i]
        c+=1
for i in range(c,n):
    l[i]=0

for i in l:
    print(i,end=" ")
