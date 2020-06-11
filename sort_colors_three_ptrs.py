l = list(map(int, input().split()))
w = 0
r = 0
b = len(l) - 1

while w<=b:
    x = l[w]
    if x == 0:
        l[r], l[w] = l[w], l[r]
        w+=1
        r+=1
    elif x == 1:
        w+=1
    else:
        l[b], l[w] = l[w], l[b]
        b-=1

print(l)
