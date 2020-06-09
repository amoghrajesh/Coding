text = input()
pattern = input()

i = len(text) - 1
j = len(pattern) - 1

while i>=0 and j>=0:
    if text[i] == pattern[j]:
        i-=1
        j-=1
    else:
        i-=1

if j == -1:
    print(True)
else:
    print(False)
