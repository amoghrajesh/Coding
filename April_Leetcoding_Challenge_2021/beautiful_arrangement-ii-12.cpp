class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> ans;
        if(!n){
            return ans;
        }
        int low = 1;
        int high = k + 1;
        for(int i = 0 ; i <= k ; i++){
            if(i%2 == 0){
                ans.push_back(low);
                low++;
            }
            else{
                ans.push_back(high);
                high--;
            }
        }
        for(int i = k+1 ; i <n ; i++)
            ans.push_back(i+1);
        
        return ans;
    }
};
