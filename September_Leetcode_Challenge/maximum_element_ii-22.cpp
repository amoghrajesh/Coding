class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        int c1, c2, first, second;
        c1 = c2 = 0;
        first = second = INT_MAX;
        
        for(int i = 0; i < n; i++){
            if(nums[i] == first){
                c1++;
            }
            else if(nums[i] == second){
                c2++;
            }
            
            else if(c1 == 0){
                c1 = 1;
                first = nums[i];
            }
            
            else if(c2 == 0){
                c2 = 1;
                second = nums[i];
            }
            
            //if the current element is none of first, second
            else{
                c1--;
                c2--;
            }
            
        }
        
        c1 = c2 = 0;
        for(int i = 0; i < n; i++){
            if(nums[i] == first){
                c1++;
            }
            else if(nums[i] == second){
                c2++;
            }
        }
        
        vector<int> ans;
        bool one = c1 > n/3;
        bool two = c2 > n/3;
        
        if(one && two){
            ans.push_back(first);
            ans.push_back(second);
        }
        else if(!one && two){
            ans.push_back(second);
        }
        else if(one && !two){
            ans.push_back(first);
        }
        return ans;
        
        
    }
};