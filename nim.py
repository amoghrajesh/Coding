from collections import Counter
def minRange(arr, n, k, b): 
    hashmap = Counter(b)
    l = 0
    r = n 
    for i in range(n): 
        s = [] 
        for j in range(i, n) : 
            if arr[j] in hashmap:
                s.append(arr[j]) 
                if (len(s) == k): 
                    if ((j - i) < (r - l)) : 
                        r = j 
                        l = i 
                    
                    break
  
        if (j == n): 
            break
    
    if l == 0 and r == n:
        return -1
    return -1 if (r - l + 1) < k else (r - l + 1)


k = 2
n = 5
m = 3

A = [1,1,1,2,1]
B = [1,2,3]

print(minRange(A, n, k, B))


