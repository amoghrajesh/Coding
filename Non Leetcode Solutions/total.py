n=int(input())
i=1
d=dict()
for i in range(n):
    a,b=list(map(int,input().split()))
    s=a+b
    d[i]=s
    i+=1
l=sorted(d.items(),key=lambda x:x[1])
for i in l:
    print(i[0]+1,end=" ")

    
