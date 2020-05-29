n=10001
n=n+1
counter=0

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
        

for i in range(1,9999999999):
    if isprime(i):
        counter+=1
    if counter==n:
        print(i)
        break

    
