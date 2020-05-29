t=int(input())
for i in range(t):
    s=input()
    l=list(s)
    a=l.count('0')
    b=l.count('1')
    if(a==1 or b==1):
        print("Yes")
    else:
        print("No")
