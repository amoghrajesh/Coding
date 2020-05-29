def score(s,u):
    if s==u:
        return len(s)
    else:
        i=0
        sc=0
        while i<n:
            #print(i)
            if s[i]==u[i]:
                sc+=1
                i+=1
            elif u[i]!='N' and s[i]!=u[i]:
                i+=2
            elif u[i]=='N':
                i+=1
        return sc
            
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    u=input()
    print(score(s,u))
