nums = [1]
index = [0]
n = len(nums)

target = [-1] * n

for i in range(n):
    print(index[i], nums[i], target)
    if target[index[i]] != -1:
        for j in range(n-1, index[i]-1, -1):
            target[j] = target[j-1]
    target[index[i]] = nums[i]
print(target)