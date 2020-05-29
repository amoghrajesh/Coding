t=int(input())
for i in range(t):
    a,b=input().split()
    a,b=int(a),int(b)
    c,d=a%10,b%10
    s=c+d
    if(s>=10):
        print(a+b-10)
    else:
        print(a+b)
