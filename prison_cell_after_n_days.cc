class Solution {
public:
    void change(vector<int>& cells, int times){
        vector<int> ans(8, 0);
        for(int i = 0;i<times;i++){
            for(int j =1;j<7;j++){
                if(cells[j-1] == cells[j+1]){
                    ans[j] = 1;
                }
                else{
                    ans[j] = 0;
                }
            }
            cells = ans;
        }
    }
    
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        if(N == 0){
            return cells;
        }
        
        change(cells, 1);
        N = (N-1)%14;
        change(cells, N);
        return cells;
    }
};