t=int(input())
for _ in range(t):
    n=int(input())
    matrix=[]
    mid=n//2
    ele=[]
    for i in range(n):
        l=list(map(int,input().split()))
        for j in l:
            ele.append(j)
        matrix.append(l)
       
    start=matrix[0][0]
    middle=matrix[mid][mid]
    if middle>start:
        print(-1)

    else:
        ele.sort(reverse=True)
        x=ele.index(middle)-ele.index(start)
        print(x)