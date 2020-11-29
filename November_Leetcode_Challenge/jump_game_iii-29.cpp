#include<queue>
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        if(!n){
            return false;
        }
        if(!arr[start]){
            return true;
        }
        
        vector<bool> visited(n, false);
        queue<int> q;
        
        q.push(start);
        visited[start] = true;
        int index;
        
        while(!q.empty()){
            index = q.front();
            q.pop();
            
            visited[index] = true;
            
            if(arr[index] == 0){
                return true;
            }
            else{
                int ahead = index + arr[index];
                int behind = index - arr[index];
                
                if(ahead <= n - 1 && !visited[ahead]){
                    q.push(ahead);
                }
                
                if(behind > -1 && !visited[behind]){
                    q.push(behind);
                }
            }
        }
        
        return false;
    }
};