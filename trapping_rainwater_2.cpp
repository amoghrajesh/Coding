#include<algorithm>
class Solution {
public:
    int trap(vector<int>& height) {
        if(!height.size()){
            return 0;
        }
        int n = height.size();
        
        vector<int> left(n, 0);
        vector<int> right(n, 0);
        
        int maxval = INT_MIN;
        
        for(int i = 0; i < n; i++){
            maxval = max(height[i], maxval);
            left[i] = maxval;
        }
        
        maxval = INT_MIN;
        
        for(int i = n - 1; i > -1; i--){
            maxval = max(height[i], maxval);
            right[i] = maxval;
        }
        
        int ans = 0;
        
        for(int i = 0; i < n; i++){
            ans += min(left[i] - height[i], right[i] - height[i]);
        }
        
        return ans;
        
    }
};