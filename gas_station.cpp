class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int tank = 0;
        int deficit = 0;
        int start = 0;
        
        for(int i = 0; i < gas.size(); i++){
            tank += gas[i] - cost[i];
            if(tank < 0){
                start = i + 1;
                deficit += tank;
                tank = 0;
            }
        }
        
        return (tank + deficit >= 0) ? start : -1;
        
    }
};