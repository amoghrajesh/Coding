class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        vector<bool> visited(100001, 0);
        
        for(int x: arr){
            visited[x] = true;
        }
        
        for(int i = 1; i <= 100001; i++){
            if(!visited[i]){
                k--;
            }
            if(k == 0){
                return i;
            }
        }
        return 100001;
    }
};