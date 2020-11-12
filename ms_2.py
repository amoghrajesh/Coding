def foo(m, n, str2, str1): 
    pos = 0
    Len = 0
    p = [0 for i in range(m + 1)] 
    k = 0
  
    for i in range(2, n + 1):  
        while (k > 0 and str1[k] != str1[i - 1]): 
            k = p[k] 
        if (str1[k] == str1[i - 1]): 
            k += 1
        p[i] = k 
      
    j = 0

    for i in range(m): 
        while (j > 0 and j < n and str1[j] != str2[i]): 
            j = p[j] 
        if (j < n and str1[j] == str2[i]): 
            j += 1
   
        if (j > Len):  
            Len = j 
            pos = i - j + 1

    return pos

str1 = "a2abccc"
str2 = "bddda2a"
n = len(str1) 
str2 = str2 + str2 
print(foo(2 * n, n, str2, str1))