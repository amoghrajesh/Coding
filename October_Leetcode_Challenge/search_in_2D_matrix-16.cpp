class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if(!m){
            return false;
        }
        int n = matrix[0].size();
        int i = 0;
        int j = n - 1;
        
        while(i < m && j > -1){
            if(matrix[i][j] == target){
                return true;
            }
            else if(matrix[i][j] < target){
                i++;
            }
            else{
                j--;
            }
        }
        
        return false;
    }
};