x=int(input())
if x<0:
    print(False)

s=str(x)
n=len(s)
h=n//2
for i in range(0,h):
    if s[i]!=s[n-1-i]:
        print(False)
        break
print(True)
        