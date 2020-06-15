Iterative:
```
struct TreeNode* searchBST(struct TreeNode* root, int val){

    struct TreeNode* temp = root;
    while(temp!=NULL){
        if(temp->val == val){
            return temp;
        }
        else if(temp->val > val){
            temp = temp->left;
        }
        else{
            temp = temp->right;
        }
    }
    return NULL;
}
```

Recursive:
```
struct TreeNode* searchBST(struct TreeNode* root, int val){
    if(root == NULL)
    {
        return NULL;
    }

    if(root->val == val){
        return root;
    }


    if(root->val > val){
        return searchBST(root->left, val);
    }

    else{
        return searchBST(root->right, val);
    }
}
```
