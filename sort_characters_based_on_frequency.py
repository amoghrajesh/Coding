from collections import Counter
s = input()
count = Counter(s).items()
count = sorted(count, key = lambda x:-x[1])
ans = ''
for i in count:
    ans += (i[0] * i[1])
print(ans)