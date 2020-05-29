original='abcdefghijklmnopqrstuvwxyz'
t,symbols=input().split()
symbols,original=list(symbols),list(original)
t=int(t)
p={'>', ';', '(', '$', ')', ',', '/', '<', '~', "'", '.', '[', '#', '{', '@', ']', '%', '-', '}', '*', '`', '!', '&', '"', '?', '^', '=', ':', '|', '+', '\\'}
for i in range(t):
    s=input()
    ans=''
    for j in s:
        if j in p:
            #print("in")
            ans+=j
        elif j=='_':
            ans+=' '
        else:
            if j.islower():
                ind=original.index(j)
                x=symbols[ind]
                ans+=x
            else:
                ind=original.index(j.lower())
                x=symbols[ind]
                ans+=(x.upper())
    print(ans)
            
    
