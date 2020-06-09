def isSub(text, pattern, m, n):
    if n == 0:
        return True
    if m == 0:
        return False

    if text[m-1] == pattern[n-1]:
        return isSub(text, pattern, m-1, n-1)

    return isSub(text, pattern, m-1, n)



text = input()
pattern = input()

print(isSub(text, pattern, len(text), len(pattern)))