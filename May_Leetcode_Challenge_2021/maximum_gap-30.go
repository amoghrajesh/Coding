func maximumGap(nums []int) int {
	n := len(nums)
	if n < 2{
		return 0
	}
	sort.Ints(nums)
	ans := 0
	for i := 0; i < n - 1; i++ {
		if nums[i + 1] - nums[i] > ans{
			ans = nums[i + 1] - nums[i]
		}
	}
	return ans
}
