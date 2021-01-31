#include<algorithm>
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        bool nextPerm = next_permutation(nums.begin(), nums.end());
    }
};