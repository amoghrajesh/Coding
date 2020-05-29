from nltk.corpus import words
allwords=set(words.words())
allwords=list(allwords)
allwords=[x for x in allwords if len(x)>3]
s="it has been woodthere is small"
s=s.split()
ans=[]
for i in s:
    temp=[]
    if i not in allwords:
        j=len(i)
        for k in range(j):
            temp.append(i[k])
            print("temp",temp)
            x=''.join(temp)
            if x in allwords:
                m=k+1
                l=list(i)
                l1=l[:m]
                l2=l[m:]
                ans.append(''.join(l1))
                ans.append('.')
                ans.append(''.join(l2))
    else:
        ans.append(i)
print(' '.join(ans))
        
    
        
