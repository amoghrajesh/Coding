class Solution {
public:
    int mirrorReflection(int p, int q) {
        int x, y, tx, ty;
        x = 0;
        y = 0;
        tx = p;
        ty = q;
        
        while(x % p != 0 || y % p != 0 || (x == 0 && y == 0)){
            x = x + tx;
            y = y + ty;
            
            tx *= -1;
            
            if(y > p || y < 0){
                ty *= -1;
                if(y > p){
                    y = p + p - y;
                }
                if(y < 0){
                    y = -y;
                }
            }
        }
        
        if(x == p && y == 0){
            return 0;
        }
        else if(x == p && y == p){
            return 1;
        }
        return 2;
    }
};