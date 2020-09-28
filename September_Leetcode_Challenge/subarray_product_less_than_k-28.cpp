class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int ans = 0;
        int start = 0;
        int end = 0;
        int prod = 1;
        int n = nums.size();
        
        for(end = 0; end < n ; end++){
            
            prod *= nums[end];
            while(start < end && prod >= k){
                prod /= nums[start];
                start++;
            }
            
            if(prod < k) ans += (1 + (end - start));
        }
        return ans;
    }
};