class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int ans = 0;
        int n = 0;
        int digits = 0;
        for(int i = 0; i<nums.size();i++){
            n = nums[i];
            digits=0;
            while(n){
                n = n/10;
                digits++;
            }
            if(digits % 2==0){
                ans++;
            }
        }
        return ans;
    }
};