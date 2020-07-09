#include <queue>
#include <algorithm>
class Solution {
public:
    typedef struct Pair{
        TreeNode* node;
        unsigned long long int level;
    }Pair;
    
    int widthOfBinaryTree(TreeNode* root) {
        
        queue<Pair> q;
        Pair p = {root, 0};
        
        q.push(p);
        unsigned long long int ans = 0;
        unsigned long long int y;
        Pair temp;
        TreeNode* x;
        
        while(!q.empty()){
            long long int size = q.size();
            ans = max(ans, q.back().level - q.front().level + 1);
            for(long long int i = 0; i< size; i++){
                temp =  q.front();
                q.pop();
                x = temp.node;
                y = temp.level;
                if(x->left){
                    q.push({x->left, 2*y});
                }
                if(x->right){
                    q.push({x->right, 2*y+1});
                }
                
            }
        }
        return ans; 
        
    }
};