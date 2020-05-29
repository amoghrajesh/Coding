t=int(input())
for i in range(t):
    n,x,s=input().split()
    n,x,s=int(n),int(x),int(s)
    k=x
    for i in range(s):
        a,b=input().split()
        a,b=int(a),int(b)
        if(k==b):
            k=a
        else:
            k=b
        print(k)
    print(k)
        
