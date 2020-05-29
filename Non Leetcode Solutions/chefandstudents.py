t=int(input())
for i in range(t):
    s=input()
    ans=''
    for j in s:
        if j=='*':
            ans+='*'
        elif j=='<':
            ans+='>'
        elif j=='>':
            ans+='<'
    #print(ans)
    x=ans.count('><')
    print(x)
    
