class Solution {
public:
    int ans = 0;
    void root_to_path(TreeNode* root, vector<int>& path){
        if(!root){
            return;
        }
        path.push_back(root->val);
        if(!root->left && !root->right){
            // check for frequency
            unordered_map<int, int> map;
            for(int x: path){
                if(map.find(x) == map.end()){
                    map[x] = 1;
                }
                else{
                    map[x]++;
                }
            }
            int c = 0;
            for(auto i = map.begin(); i != map.end(); i++){
                if(i->second % 2 == 1){
                    c++;
                }
            }
            if(c <= 1){
                ans++;
            }
        }
        // path.push_back(root->val);
        
        root_to_path(root->left, path);
        root_to_path(root->right, path);
        
        path.pop_back();
    }
    
    int pseudoPalindromicPaths (TreeNode* root) {
        vector<int> path;
        root_to_path(root, path);
        return ans;
    }
};