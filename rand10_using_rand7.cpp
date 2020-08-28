class Solution {
public:
    int rand10() {
        int row, col, val;
        row = rand7();
        col = rand7();
        val = col + (row - 1) * 7;
        
        while(val >= 41){
            row = rand7();
            col = rand7();
            val = col + (row - 1) * 7;
        }
        return 1 + (val - 1) % 10;
        
    }
};