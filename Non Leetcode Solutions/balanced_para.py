n=int(input())
p=list(map(int,input().split()))
stack=[]
if p[0]<0:
    print(0)
else:
    c=0
    for i in p:
        if i>0:
            stack.append(i)
        elif i<0 and i==-1*(stack[-1]):
            stack.pop()
            c+=2
        elif i<0 and i!=-1*stack[-1]:
            break
    print(c)
        
