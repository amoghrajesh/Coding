t=int(input())
for i in range(t):
    n,k=input().split()
    n,k=int(n),int(k)
    old=input().split()
    new=[]
    ans=[]
    print("old",old)
    for j in range(k):
        s=input()
        s1=s[2:]
        new.append(s1)
    print("new",new)
    for j in old:
        for k in new:
            if(k.find(j)>=0):
                ans.append("YES")
                break
            else:
                ans.append("NO")
                break
    print(ans)
            
        
    
