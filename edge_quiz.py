def example(L):
    x = 0
    result = []
    while x < len(L):
        result.append(L[x+1])
        x = x + 2
    return result
print (example([19,2,13,4]))