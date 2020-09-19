#include<queue>
class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        queue<int> q;
        for(int i = 1; i <= 9; i++){
            q.push(i);
        }
        int cur, temp;
        vector<int> ans;
        while(!q.empty()){
            cur = q.front();
            q.pop();
            if(cur >= low && cur <= high){
                ans.push_back(cur);
            }
            if(cur % 10 != 9){
                temp = cur * 10 + ((cur % 10) + 1);
                q.push(temp);
            }
        }
        return ans;
    }
};