nums1 = [2,1,3]
nums2 = [2,3,1]
stack = [nums2[0]]
hashmap = dict()
ans = []
for i in range(1, len(nums2)):
    while stack and stack[-1]<nums2[i]:
        p = stack.pop()
        hashmap[p] = nums2[i]
    stack.append(nums2[i])
for i in nums1:
    ans.append(hashmap.get(i, -1))
print(ans)
