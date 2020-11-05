class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int even = 0;
        int odd = 0;
        
        for(int x: position){
            if(x % 2){
                odd++;
            }
            else{
                even++;
            }
        }
        
        int cost_to_move_odd_to_even = odd * 1;
        int cost_to_move_even_to_odd = even * 1;
        
        return min(cost_to_move_odd_to_even, cost_to_move_even_to_odd);
        
    }
};