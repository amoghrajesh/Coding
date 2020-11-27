class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        if(!n){
            return false;
        }
        
        int sum = 0;
        for(int x: nums){
            sum += x;
        }
        
        int part1 = sum/2;
        int part2 = sum - part1;
        
        if(part1 != part2){
            return false;
        }
        
        bool dp[part1 + 1][n + 1];
        
        for(int i = 1; i < part1 + 1; i++){
            dp[i][0] = false;
        }
        
        for(int i = 0; i < n + 1; i++){
            dp[0][i] = true;
        }
        
        for(int i = 1; i < part1 + 1; i++){
            for(int j = 1; j < n + 1; j++){
                dp[i][j] = false;
            }
        }
        
        for(int i = 1; i < part1 + 1; i++){
            for(int j = 1; j < n + 1; j++){
                if (i >= nums[j - 1])
                    dp[i][j] = dp[i][j - 1]
                                 || dp[i - nums[j - 1]][j - 1];
            }
        }
        
        return dp[part1][n];
    }
};