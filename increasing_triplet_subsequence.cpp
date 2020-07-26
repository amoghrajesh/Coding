class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int small, big;
        small = big = INT_MAX;
        for(int i: nums){
            if(i <= small){
                small = i;
            }
            else if(i <= big){
                big = i;
            }
            else{
                return true;
            }
        }
        return false;
    }
};