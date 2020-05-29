t=int(input())
for i in range(t):
    n=int(input())
    b=bin(n)[2:]
    part=b[:12]
    part2=b[12:]
    ans=0
    ans+=part.count('1')
    for j in range(len(part2)):
        ans+=int(pow(2,j))
    print(ans)
    
