t=int(input())
for k in range(t):
    x=input()
    n=int(input())
    l=[]
    for j in range(n):
        y=int(input())
        l.append(y)
    c=0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                c+=1
    print(c)
x=input()
        
