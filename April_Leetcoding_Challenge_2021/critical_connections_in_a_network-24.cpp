class Solution {
public:
    void findBridge(int node, int &timer, int parent, vector<vector<int>> &connections, vector<vector<int>> &ans, vector<int> &in, vector<int> &low,unordered_map<int,int> &vis) {
        vis[node] = 1;
        in[node] = timer;
        low[node] = timer;
        timer+=1;
        for(auto child: connections[node]) {
            if(child == parent) continue;
            if(vis[child] == 1) {
                //backEdge
                low[node] = min(low[node], in[child]);
            }else {
                findBridge(child,timer, node, connections, ans, in, low, vis);
                if(low[child] > in[node]) {
                    ans.push_back({node, child});
                }
                
                low[node] = min(low[node], low[child]);
            }
        }
    }
    
    
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<vector<int>> ans;
        vector<int> in(n), low(n);
        unordered_map<int,int> vis;
        vector<vector<int>> g(n+1);
        for(auto c: connections){
            g[c[0]].push_back(c[1]);
            g[c[1]].push_back(c[0]);
        }
        int timer = 0;
        findBridge(0, timer, -1, g, ans, in, low, vis);
        return ans;
    }
};
