class Solution {
public:
    int filter(vector<int> &nums){
        int j = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] <= 0){
                swap(nums[i], nums[j]);
                j++;
            }
        }
        return j;
    }
    int firstMissingPositive(vector<int>& nums) {
        long int offset = filter(nums);
        cout << "offset: " << offset << "\n";
        for(long int i = offset; i < nums.size(); i++){
            long int idx = abs(nums[i]) - 1 + offset;
            if(idx >= offset && idx < nums.size() && nums[idx] > 0){
                nums[idx] *= -1;
            } 
        }
        for(int v: nums){
            cout << v << " ";
        }
        
        for(long int i = offset; i < nums.size(); i++){
            if(nums[i] > 0){
                return i + 1 - offset;
            }
        }
        return nums.size() - offset + 1;
    }
};