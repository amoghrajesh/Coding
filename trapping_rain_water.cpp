#include<algorithm>
class Solution {
public:
    int trap(vector<int>& height) {
        if(!height.size()){
            return 0;
        }
        int n = height.size();
        int ans = 0;
        int leftMax = 0;
        int rightMax = 0;
        
        for(int i = 1; i < n - 1; i++){
            leftMax = height[i];
            rightMax = height[i];
            
            for(int j = 0; j < i; j++){
                leftMax = max(leftMax, height[j]);
            }
            
            for(int j = i + 1; j < n; j++){
                rightMax = max(rightMax, height[j]);
            }
            
            ans += min(leftMax - height[i], rightMax - height[i]);
        }
        return ans;
        
        
    }
};