class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long first, second, third;
        first = second = third = LONG_MIN;
        for(int i: nums){
            if(i > first){
                third = second;
                second = first;
                first = i;
            }
            else if(i > second && i < first){
                third = second;
                second = i;
            }
            else if(i > third && i < second){
                third = i;
            }
        }
        
        return third != LONG_MIN ? third : *max_element(nums.begin(), nums.end());
    }
};