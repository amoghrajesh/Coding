class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int num_i = INT_MAX;
        for(int j = 0; j < nums.size(); j++){
            if(nums[j] < num_i){
                num_i = nums[j];
            }
            for(int k = j + 1; k < nums.size(); k++){
                if(num_i < nums[k] && nums[k] < nums[j]){
                    return true;
                }
            }
            
        }
        return false;
    }
};