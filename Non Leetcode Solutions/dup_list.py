l=["abc","abc","abc","def","def","zx","kl"]
ans=[]
j=0
for i in range(len(l)):
    if i+1<len(l) and l[i]==l[i+1]:
        j=i
        while j<len(l) and l[j]==l[i]:
            l[j]='z'
            j+=1
for i in l:
    if i!='z':
        ans.append(i)
print(' '.join(ans))
    
