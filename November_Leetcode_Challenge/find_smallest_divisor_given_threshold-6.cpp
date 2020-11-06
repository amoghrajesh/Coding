#include<cmath>
class Solution {
public:
    int divide_sum(vector<int>& nums, int x){
        int s = 0;
        for (int n : nums) {
            s += n / x + (n % x == 0 ? 0 : 1); 
        }
        return s;
    }
    
    int smallestDivisor(vector<int>& nums, int threshold) {
        int l = 1;
        int r = nums[nums.size() - 1];
        vector<int> mins;
        
        while(l <= r){
            int m = l + (r - l)/2;
            int s = divide_sum(nums, m);
            if(s <= threshold){
                mins.push_back(m);
                r = m - 1;
            }
            else{
                l = m + 1;
            }
        }
        return *min_element(mins.begin(), mins.end());
    }
};