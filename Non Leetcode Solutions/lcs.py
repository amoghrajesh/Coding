def subseq(x,y,m,n):
    L=[[0 for x in xrange(n+1)] for y in xrange(m+1)]
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif x[i-1]==y[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    index=L[m][n]
    lcs=[""]*(index+1)
    lcs[index]=""
    i=m
    j=n
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            lcs[index-1]=x[i-1]
            i-=1
            j-=1
            index-=1
        elif L[i-1][j]>L[i][j-1]:
            i-=1
        else:
            j-=1
    print("".join(lcs))            

    
m,n=input().split()
m,n=int(n),int(m)
x=list(input().split())
y=list(input().split())
subseq(x,y,m,n) #x m y n
