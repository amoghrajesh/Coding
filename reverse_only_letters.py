s = input()
s = list(s)
i = 0
j = len(s) - 1
while i<j:
    if s[i].isalpha() and s[j].isalpha():
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1
    elif not s[i].isalpha():
        i+=1
    elif not s[j].isalpha():
        j-=1
print(''.join(s))