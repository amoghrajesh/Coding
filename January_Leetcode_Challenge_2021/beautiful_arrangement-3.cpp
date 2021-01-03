class Solution {
public:
    int ans = 0;
    
    void dfs(vector<bool>& visited, int n, int i){
        if(i > n){
            ans++;
            return;
        }
        
        for(int j = 1; j <= n; j++){
            if(!visited[j] && (!(i % j) || !(j % i))){
                visited[j] = true;
                dfs(visited, n, i + 1);
                visited[j] = false;
            }
        }
        return;
    }
    
    int countArrangement(int n) {
        vector<bool> visited(n + 1, false);
        int i = 1;
        dfs(visited, n, i);
        return ans;
    }
};