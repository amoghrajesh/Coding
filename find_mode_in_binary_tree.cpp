class Solution {
public:
    unordered_map<int, int> map;
    void inorder(TreeNode* root){
        if(!root){
            return;
        }
        inorder(root->left);
        
        if(map.find(root->val) == map.end()){
            map[root->val] = 1;
        }
        else{
            map[root->val]++;
        }
        
        inorder(root->right);
    }
    vector<int> findMode(TreeNode* root) {
        inorder(root);
        int m = INT_MIN;
        for(auto i = map.begin(); i != map.end(); i++){
            if(i->second > m){
                m = i->second;
            }
        }
        vector<int> ans;
        cout << m;
        
        for(auto i = map.begin(); i != map.end(); i++){
            if(i->second == m){
                ans.push_back(i->first);
            }
        }
        return ans;
    }
};