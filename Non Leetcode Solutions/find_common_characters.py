from collections import Counter
l = ["bella", "label", "roller"]
c = Counter(l[0])
s1 = set(l[0])
for i in range(1, len(l)):
    s = l[i]
    s2 = set(s)
    c1 = Counter(s)
    for k in c:
        if k in c1:
            s1 = s1.intersection(s2)
            c[k] = min(c[k], c1[k])
ans = []
for i in s1:
    f = c[i]
    for j in range(f):
        ans.append(i)
print(ans)