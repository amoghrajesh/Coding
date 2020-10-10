class Solution {
public:
    static bool comp(vector<int> &a, vector<int> &b){
        return a[1] < b[1];
    }
    
    int findMinArrowShots(vector<vector<int>>& points) {
        int n = points.size();
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return 1;
        }

        int ans = 1;
        sort(points.begin(), points.end(), comp);
        int endPos = points[0][1];
        
        for(int i = 1; i < n; i++){
            if(endPos < points[i][0]){
                ans += 1;
                endPos = points[i][1];
            }
        }
        
        return ans;
        
    }
};