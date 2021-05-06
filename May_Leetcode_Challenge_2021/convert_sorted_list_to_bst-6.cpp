class Solution {
public:
    TreeNode* root;
    TreeNode* dfs(vector<int> &v, int l, int r){
        if(l == r){
            return new TreeNode(v[l]);
        }
        if(l > r){
            return NULL;
        }
        
        int m = (l + (r - l)/2);
        TreeNode* temp = new TreeNode(v[m]);
        temp->left = dfs(v, l, m - 1);
        temp->right = dfs(v, m + 1, r);
        return temp;
    }
    
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> v;
        ListNode* p = head;
        
        while(p){
            v.push_back(p->val);
            p = p->next;
        }
        
        int n = v.size();
        root = dfs(v, 0, n - 1);
        
        return root;
    }
};
