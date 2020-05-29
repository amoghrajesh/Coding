t=int(input())
for i in range(t):
    s=input()
    l=s.split()
    if  len(l)==1:
        print(s[0].upper()+s[1:].lower())
    elif len(l)==2:
        ans=''
        x=l[0]
        ans+=x[0].upper()
        ans+='. '
        ans+=(l[1][0].upper()+l[1][1:].lower())
        print(ans)
    else:
        ans=''
        ans+=(l[0][0].upper()+'. ')
        ans+=(l[1][0].upper()+'. ')
        ans+=(l[2][0].upper()+l[2][1:].lower())
        print(ans)
        
        
