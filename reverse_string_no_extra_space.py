l = ["H","a","n","n","a","h"]
n = len(l)
for i in range(n//2):
    l[i], l[n-1-i] = l[n-1-i], l[i]
print(l)