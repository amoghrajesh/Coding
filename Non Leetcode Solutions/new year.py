t=int(input())
for i in range(t):
    n=int(input())
    sums=0
    count=0
    arr=list(map(int,input().split()))
    for i in range(n-1):
        count=0
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                count+=1
        if count>2:
            print("Too chaotic")
            quit()
        else:
            sums+=count
    print(sums)
