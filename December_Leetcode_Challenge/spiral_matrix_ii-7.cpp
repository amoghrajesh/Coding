class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> a;
        for(int i = 0; i < n; i++){
            vector<int> v(n, 0);
            a.push_back(v);
        }
        
        int v = 1;
        int sr, er, sc, ec;
        
        sr = sc = 0;
        er = ec = n;
        
        while(sr < er && sc < ec){
            for(int i = sc; i < ec; i++){
                a[sr][i] = v;
                v++;
            }
            sr++;
            
            for(int i = sr; i < er; i++){
                a[i][ec - 1] = v;
                v++;
            }
            ec--;
            
            if(sr < er){
                for(int i = ec - 1; i >= sc; i--){
                    a[er - 1][i] = v;
                    v++;
                }
                er--;
            }
            
            if(sc < ec){
                for(int i = er - 1; i >= sr; i--){
                    a[i][sc] = v;
                    v++;
                }
                sc++;
            }
        }
        return a;
    }
};