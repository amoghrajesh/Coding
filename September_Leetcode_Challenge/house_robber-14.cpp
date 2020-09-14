class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return nums[0];
        }
        vector<int> dp;
        dp.push_back(nums[0]);
        dp.push_back(max(nums[0], nums[1]));
        
        if(n <= 2){
            return dp[n-1];
        }
        int temp;
        for(int i = 2; i < n; i++){
            temp = max(dp[i-1], dp[i-2] + nums[i]);
            dp.push_back(temp);
        }
        
        return dp[n-1];
        
        
    }
};