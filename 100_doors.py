a = [1] * 101

for every in range(2, 102):
    j = every
    while j < 102:
        if j < 102:
            a[j] = abs(a[j] - 1)
        j += every
for i in range(1, 102):
    if a[i]:
        print(i)