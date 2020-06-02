s = input()
t = input()
k = int(input())
prefixLength = 0
if len(s) + len(t) <=k:
    print("Yes")
else:
    for si,ti in zip(s,t):
        if si==ti:
            prefixLength+=1
        else:
            break

    del_s = len(s) - prefixLength
    add_t = len(t) - prefixLength

    if del_s+add_t<=k:
        print("Yes")
    else:
        print("No")

