from collections import Counter
s1=input()
s2=input()

h1=Counter(s1)
lens1=len(s1)
lens2=len(s2)

for i in range(lens2-lens1+1):
    temp=s2[i:i+lens1]
    h2=Counter(temp)
    if h2==h1:
        print(True)
print(False)


