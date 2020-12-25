class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        if(!matrix.size()){
            return ans;
        }
        
        int m = matrix.size();
        int n = matrix[0].size();
        int i = 0; int j = 0;
        bool moveup = true;
        
        ans.push_back(matrix[i][j]);
        
        while(i < m - 1 || j < n - 1){
            if(moveup){
                if(j == n - 1){
                    i++;
                    moveup = !moveup;
                }
                // come to end of iteration
                else if(i == 0){
                    j++;
                    moveup = !moveup;
                }
                else{
                    i--;
                    j++;
                }
            }
            else{
                if(i == m - 1){
                    j++;
                    moveup = !moveup;
                }
                // come to end of iteration
                else if(j == 0){
                    i++;
                    moveup = !moveup;
                }
                else{
                    i++;
                    j--;
                }
            }
            
            ans.push_back(matrix[i][j]);
        }
        return ans;
    }
};