class Solution {
public:
    int maxArea(vector<int> &height) {
        int area = INT_MIN;
        int l = 0;
        int r = height.size() - 1;
        int a, m;
        
        while(l < r){
            m = min(height[l], height[r]);
            a = m * (r - l);
            area = max(area, a);
            if(m == height[l]){
                l++;
            }
            else{
                r--;
            }
        }
        return area;
    }
};
