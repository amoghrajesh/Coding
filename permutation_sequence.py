from math import factorial
n = int(input())
k = int(input())

nums = list(range(1, n + 1))
ans = ""

while len(nums)>1:
    f = factorial(len(nums) - 1)
    block =  k//f
    k -= block*f
    if k == 0:
        block-=1
    digit = nums[block]
    ans += str(digit)
    nums.remove(digit)
ans += str(nums[0])
print(ans)
