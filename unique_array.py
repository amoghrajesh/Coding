l = list(map(int,input().split()))
n = len(l)
if n==len(set(l)):
    print(True)
else:
    print(False)