t=int(input())
for i in range(t):
    x=input()
    y=input()
    flag=0
    for j in range(len(x)):
        if(x[j]=='?' or y[j]=='?'):
            pass
        else:
            if(x[j]!=y[j]):
                print("No")
                flag=1
                break
    if(flag==0):
        print("Yes")
