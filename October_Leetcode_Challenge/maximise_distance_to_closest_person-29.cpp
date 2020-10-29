class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int n = seats.size();
        int ans = INT_MIN;
        int left, right;
        int d1, d2;
        
        for(int i = 0; i < n; i++){
            if(seats[i] == 0){
                left = right = i;
                while(left >= 0 && seats[left] != 1){
                    left--;
                }
                
                if(left < 0){
                    d1 = INT_MAX;
                }
                else{
                    d1 = i - left;
                }
                
                while(right < n && seats[right] != 1){
                    right++;
                }
                
                if(right >= n){
                    d2 = INT_MAX;
                }
                else{
                    d2 = right - i;
                }
                
                int local = min(d1, d2); //closest of left and right
                
                if(local > ans){
                    ans = local;
                }
                
            }
        }
        
        return ans;
    }
};