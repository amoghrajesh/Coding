class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int j;
        int till_here;
        for(int i = 0; i < n; i++){
            j = (i + 1) % n;
            till_here = gas[i] - cost[i];
            while(j != i){
                if(till_here <= 0){
                    break;
                }
                till_here += (gas[j] - cost[j]);
                j = (j + 1) % n;
            }
            if(j == i && till_here >= 0){
                return i;
            }
        }
        return -1;
    }
};