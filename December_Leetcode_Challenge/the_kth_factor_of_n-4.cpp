class Solution {
public:
    int kthFactor(int n, int k) {
        int j = 0;
        for(int i = 1; i <= n; i++){
            if(!(n % i)){
                j++;
            }
            if(j == k){
                return i;
            }
        }
        return -1;
    }
};