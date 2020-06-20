s = "loveleetcode"
c = 'e'

indexes = []

for i in range(len(s)):
    if s[i] == c:
        indexes.append(i)

ans = []
for i in range(len(s)):
    if s[i] == c:
        ans.append(0)
    
    else:
        m = 9999
        for j in indexes:
            if abs(i - j) < m:
                m = abs(i - j)
        ans.append(m)
print(ans) 

