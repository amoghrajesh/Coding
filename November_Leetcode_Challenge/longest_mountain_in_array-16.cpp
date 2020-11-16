class Solution {
public:
    int longestMountain(vector<int>& A) {
        int n = A.size();
        if(n < 3){
            return 0;
        }
        
        vector<int> left(n, 0);
        vector<int> right(n, 0);
        
        for(int i = 1; i < n; i++){
            if(A[i] > A[i-1]){
                left[i] = left[i-1] + 1;
            }
        }
        
        for(int i = n - 2; i > 0; i--){
            if(A[i] > A[i + 1]){
                right[i] = right[i+1] + 1;
            }
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            if(left[i] && right[i]){
                ans = max(ans, left[i] + right[i] + 1);
            }
        }
        return ans;
    }
};