def ans(X, K, S, N):
    # Write your code here
    bl=[]
    a=N//X
    k=0
 
    i=1
    while(True):
        st=(i-1)*X+1
        end=min(N,i*X)
        temp=list(set(S[st-1:end]))
        temp.sort()
        bl.append(temp)
        if end==N:
            break
        i+=1
    
    
    tot=1
    for i in bl:
        tot*=len(i)
 
    s=""
    k=0
    L=K
    while(k<len(bl)):
        tot=tot//len(bl[k])
        b=int(K//tot)
        s+=str(bl[k][b])
        k+=1
        K%=tot
 
    return s
n = 10
x = 5 
k = 10
s = "1234567891"
print(ans(x, k - 1, s, n))