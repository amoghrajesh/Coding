class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        double matrix[101][101] = {0};
        matrix[0][0] = (double)poured;
        
        for(int i = 0; i <= query_row; i++){
            for(int j = 0; j <= query_glass; j++){
                double overflowed = (matrix[i][j] - 1.0)/2.0;
                if(overflowed > 0.0){
                    matrix[i+1][j] += overflowed;
                    matrix[i+1][j+1] += overflowed;
                }
            }
        }
        
        return min(1.0, matrix[query_row][query_glass]);
    }
};