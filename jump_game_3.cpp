class Solution {
public:
    bool solve(vector<int>& arr, int start, vector<int> &visited){
        if(start < 0 || start >= arr.size()){
            return false;
        }
        if(visited[start]){
            return false;
        }
        visited[start] = 1;
        if(arr[start] == 0){
            return true;
        }
        return solve(arr, start + arr[start], visited) || solve(arr, start - arr[start], visited);
        
    }
    
    bool canReach(vector<int>& arr, int start) {
        vector<int> visited(arr.size(), 0);
        return solve(arr, start, visited);
    }  
};