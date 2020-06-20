s = "loveleetcode"
c = "e"
ans = []
for i in range(len(s)):
    if s[i] == c:
        ans.append(0)
    else:
        left = i - 1
        right = i + 1
        leftFound = 0
        rightFound = 0
        leftDist = 10**9
        rightDist = 10**9
        while left>-1 and right<len(s)-1:
            if leftFound and rightFound:
                break
            
            if s[left] == c:
                leftDist = i - left
                leftFound = 1
            
            if s[right] == c:
                rightDist = right - i
                rightFound = 1
            
            left -= 1
            right += 1
        
        ans.append(min(leftDist, rightDist))
print(ans)