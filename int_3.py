def foo(s1, s2, k): 
    n = len(s1) 
    s1 = list(s1) 
    s2 = list(s2) 
      
    for i in range(n): 
        diff = ord(s2[i]) - ord(s1[i]) 
        if diff == 0: 
            continue
        if diff < 0: 
            diff = diff + 26
        if diff > k: 
            return False
      
    return True

s1 = "abc"
s2 = "ddd"
k = 3
result = foo(s1, s2, k)  
if result: 
    print("YES") 
else: 
    print("NO") 