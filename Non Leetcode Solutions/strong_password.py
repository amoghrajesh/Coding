n = int(input())
s = input()
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

bn = 0
bl = 0
bu = 0
bsp = 0

for i in s:
    if i in numbers:
        bn = 1
    elif i in lower_case:
        bl = 1
    elif i in upper_case:
        bu = 1
    else:
        bsp = 1


ans = (not bn) + (not bl) + (not bu) + (not bsp)
if (n + ans) >=6:
    print(ans)
else:
    print(6-n)


