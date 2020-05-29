t=int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    words=input().split()
    #print(words)
    sen=[]
    for i in range(k):
        s=input()
        s=s.split()
        s=s[1:]
        sen.append(s)
    ans=[]
    for i in words:
        count=0
        print(i)
        for j in sen:
            if i in j:
                count+=1
                print('YES')
                break
        if count==0:
            print('NO')
                
        
        
