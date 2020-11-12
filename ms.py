gindex, start, end = list(map(int,input().split()))
b = bin(gindex)[2:].zfill(32)
ans = ''
for i in range(0, 32 - end):
    ans += b[i]
for i in range(32- end, 32 - start + 1):
    if b[i] == '0':
        ans += '1'
    else:
        ans += '0'
for i in range(32 - start + 1, 32):
    ans += b[i]
print(int(ans, 2))
