t=int(input())
for i in range(t):
    s=input()
    x=s[::-1]
    if(s==x):
        print("wins")
    else:
        print("losses")
