x = int(input())
y = int(input())
ans = 0
while x!=0 and y!=0:
    print("x and y: ",x,y)
    a = x % 2
    b = y % 2
    if a!=b:
        ans+=1
    x//=2
    y//=2

print(x,y)
# x got to zero
while y!=0:
    a = y % 2
    if a == 1:
        ans+=1
    y//=2
while x!=0:
    a = x % 2
    if a == 1:
        ans+=1
    x//=2
print(ans)

