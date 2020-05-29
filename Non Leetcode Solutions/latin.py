t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    s3=list(s1)
    s4=list(s2)
    small=0
    big=0
    for i in range(len(s3)):
        if(s3[i]=='?' or s4[i]=='?'):
            s3[i]='x'
            s4[i]='x'
    for i in range(len(s3)):
        if(s3[i]!=s4[i]):
            small+=1
    print(small)

    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            big+=1
    for j in range(len(s1)):
        if(s1[j]=='?' and s2[j]=='?'):
            big+=1
    print(big)
        
            
            
