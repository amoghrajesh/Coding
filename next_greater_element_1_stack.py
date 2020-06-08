nums1 = [2,1,3]
nums2 = [2,3,1]
n = len(nums2)
stack = []
ans = []
for i in nums1:
    stack = []
    j = n - 1
    while nums2[j] != i:
        if nums2[j] > i:
            stack.append(nums2[j])
        j -= 1
    if stack:
        ans.append(stack.pop())
    else:
        ans.append(-1)
print(ans)