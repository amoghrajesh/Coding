class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        if(A.size() == 0){
            return A;
        }
        
        int l = 0;
        int r = A.size() - 1;
        
        while(l < r){
            //while left is even, go ahead
            while(l < r && A[l] % 2 == 0){
                l++;
            }
            //while right is odd, get back
            while(l < r && A[r] % 2 == 1){
                r--;
            }
            swap(A[l], A[r]);
        }
        
        return A;
    }
};