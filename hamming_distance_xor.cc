class Solution {
public:
    int hammingDistance(int x, int y) {
        int z = x ^ y;
        int b = 0;
        int ans = 0;
        while(z){
            b = z % 2;
            if(b){
                ans+=1;
            }
            z = z/2;
        }
        return ans;
    }
};