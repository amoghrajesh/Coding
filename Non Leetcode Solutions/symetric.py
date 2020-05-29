t=int(input())
for i in range(t):
    n=int(input())
    mat=[]
    #print(mat)
    for p in range(n):
        s=input()
        l=[]
        for i in s:
            l.append(i)
            
            
        mat.append(l)
    #print(mat)
    h=1
    v=1
    for row in range(n//2):
        for col in range(n):
            #print(row,col)
            if mat[row][col]!=mat[n-1-row][col]:
                h=0

    for col in range(n//2):
        for row in range(n):
            if mat[col][row]!=mat[n-1-col][row]:
                v=0
    if h==0 and v==0:
        print("NO")
    elif h==0 and v==1:
        print("VERTICAL")
    elif h==1 and v==0:
        print("HORIZONTAL")
    else:
        print("BOTH")
        

    
