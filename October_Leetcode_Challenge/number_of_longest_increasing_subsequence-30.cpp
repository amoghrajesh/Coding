class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        if(n == 0){
            return 0;
        }
        
        vector<int> end(n, 1);
        vector<int> count(n, 1);
        
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if(nums[i] > nums[j]){
                    if(end[i] < end[j] + 1){
                        end[i] = end[j] + 1;
                        count[i] = count[j];
                    }
                    else if(end[i] == end[j] + 1){
                        count[i] += count[j];
                    }
                }
            }
        }
        
        int m = *max_element(end.begin(), end.end());
        int ans = 0;
        
        for(int i = 0; i < n; i++){
            if(end[i] == m){
                ans += count[i];
            }
        }
        
        return ans;
    }
};