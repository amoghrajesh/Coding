n = int(input())
s = str(n)
d = 0
p = 1

for i in s:
    d+=int(i)
    p*=int(i)
print(p-d)
    
