t = int(input())
s = input()

n = len(s)
ans = 0
start = 0
maxlength = 1

for i in range(n):
    for j in range(i, n):
        m = j - i + 1
        flag = 1
        for k in range(m//2):
            if s[i+k] != s[j-k]:
                flag = 0
        if flag and j-i+1 > ans:
            maxlength = j-i+1
            start = i
print(s[start: start + maxlength - 1])