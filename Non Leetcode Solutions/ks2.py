t=int(input())
def ans(n):
    return 10*n+(10-(sum(map(int,str(n))))%10)
for i in range(t):
    n=int(input())
    print(ans(n))
