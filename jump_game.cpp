class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<int> flag(nums.size(), 0);
        flag[0] = 1;
        int maxJump;
        
        for(int i = 0; i < nums.size(); i++){
            //mark all the positions reachable from here
            if(flag[i] && nums[i] > 0){
                maxJump = nums[i];
                for(int j = 1; j <= maxJump; j++){
                    if(i + j < nums.size()){
                        flag[i + j] = true;
                    }
                }
            }  
        }
        return flag[nums.size() - 1];
        
    }
};