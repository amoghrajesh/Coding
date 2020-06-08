#if n is a power of two, then n&(n-1) == 0
n = int(input())
if n==1:
    print("Yes")
else:
    b = bin(n)[2:]
    ones = b.count('1')
    if ones == 1 and b[-1]!='1':
        print("Yes")
    else:
        print("No")