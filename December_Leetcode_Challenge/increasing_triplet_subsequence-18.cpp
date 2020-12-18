class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        vector<int> left(nums.size(), -1);
        vector<int> right(nums.size(), -1);
        
        int n = nums.size();
        left[0] = nums[0];
        right[n - 1] = nums[n - 1];
        
        for(int i = 1; i < n; i++){
            left[i] = min(left[i - 1], nums[i]);
        }
        
        for(int i = n - 2; i > -1; i--){
            right[i] = max(right[i + 1], nums[i]);
        }
        
        for(int i = 0; i < n; i++){
            if(left[i] < nums[i] && right[i] > nums[i]){
                return true;
            }
        }
        return false;
    }
};