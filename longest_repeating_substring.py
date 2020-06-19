s = input()
subs = dict()
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i:j+1] not in subs:
            subs[s[i:j+1]] = 1
        else:
            subs[s[i:j+1]] += 1
l = 0
ans = ""
for sub in subs:
    length = len(sub)
    if length > l and subs[sub] >= 2:
        ans = sub
        l = length

print(ans)       