nums1 = [2,4]
nums2 = [1,2,3,4]
ans = []
for i in nums1:
    b = 0
    for j in range(nums2.index(i)+1, len(nums2)):
        if b == 0 and nums2[j]>i:
            b = 1
            ans.append(nums2[j])
    if b == 0:
        ans.append(-1)
print(ans)