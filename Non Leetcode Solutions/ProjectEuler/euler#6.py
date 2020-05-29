def sosq(n):
    return n*(n+1)*(2*n+1)//6

def son(n):
    return n*(n+1)//2


n=10
s=sosq(n)
s1=son(n)

print(s1**2-s)
