class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int m = flowerbed.size();
        if(m == 0) return false;
        
        if(m == 1 && flowerbed[0] == 0 && n == 1){
            return true;
        }
        
        for(int i = 0; i < m; i++){
            if(flowerbed[i] == 0 && (i == 0 || !flowerbed[i - 1]) && (i == m - 1 || !flowerbed[i + 1])){
                flowerbed[i] = 1;
                n--;
            }
            
            if(n <= 0){
                return true;
            }
        }
        return false;
    }
};