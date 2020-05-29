def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

s=0
for i in range(2,2000000):
    if isprime(i):
        s+=i
print(s)
        
