class Solution {
public:
    map<int, vector<pair <int, int>>> m;
    
    void dfs(TreeNode* root, int x, int y){
        if(!root){
            return;
        }
        
        m[x].push_back({y, root->val});
        dfs(root->left, x - 1, y + 1);
        dfs(root->right, x + 1, y + 1);
    }
    
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        m.clear();
        dfs(root, 0, 0);
        
        vector<vector<int>> ans;
        vector<int> level;
        
        for(auto iter: m){
            level.clear();
            sort(iter.second.begin(), iter.second.end());
            for(auto pair: iter.second){
                level.push_back(pair.second);
            }
            ans.push_back(level);
        }
        return ans;
    }
};
