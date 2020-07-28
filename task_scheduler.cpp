#include <algorithm>
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26,0);
        for(char c: tasks){
            count[c - 'A']+=1;
        }
        
        sort(count.begin(), count.end());
        int most_frequent = count[25] - 1;
        int available_slots = most_frequent * n;
        
        for(int i = 24; i > -1; i--){
            available_slots -= min(count[i], most_frequent);
        }
        
        return available_slots > 0 ? tasks.size() + available_slots : tasks.size();
        
        
    }
};