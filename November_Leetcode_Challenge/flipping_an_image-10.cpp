class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int n = A.size();
        if(!n){
            return A;
        }
        int m = A[0].size();
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m / 2; j++){
                if(A[i][j] == A[i][m - 1 - j]){
                    int temp = A[i][j];
                    A[i][j] = (int)(!temp);
                    A[i][m - 1 -j] = (int)(!temp);
                }
            }
            if(m % 2 == 1){
                A[i][m / 2] = (int)(!A[i][m / 2]);
            }
        }
        return A;
        
    }
};