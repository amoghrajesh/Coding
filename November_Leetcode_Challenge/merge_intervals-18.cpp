class Solution {
public:
    static bool comp(vector<int> a, vector<int> b){
        return a[0] < b[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        int index = 0;
        
        sort(intervals.begin(), intervals.end(), comp);
        
        for(int i = 1; i < n; i++){
            //overlap
            if(intervals[index][1] >= intervals[i][0]){
                intervals[index][0] = min(intervals[index][0], intervals[i][0]);
                intervals[index][1] = max(intervals[index][1], intervals[i][1]);
            }
            else{
                ++index;
                intervals[index] = intervals[i];
            }
        }
        vector<vector<int>> ans;
        for(int i = 0; i <= index; i++){
            ans.push_back(intervals[i]);
        }
        return ans;
    }
};