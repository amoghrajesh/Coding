t=int(input())
vow=['a','e','i','o','u']
for i in range(t):
    n=int(input())
    s=input()
    a=list(s)
    c=0
    for j in range(n-1):
        if(a[j] not in vow):
            if(a[j+1] in vow):
                c+=1
    print(c)
                
