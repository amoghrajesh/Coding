class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int i = 0;
        int n = arr.size();
        
        if(n < 3){
            return false;
        }
        
        int peak = -1;
        
        while(peak == -1 && i < n - 1){
            if(arr[i] > arr[i + 1]){
                peak = i;
            }
            i++;
        }
        cout << peak << "\n";
        if(peak == -1 || peak == 0 || peak == n - 1){
            return false;
        }
        
        i = 0;
        bool incr = true;
        
        while(incr && i < peak){
            if(arr[i + 1] <= arr[i]){
                incr = false;
            }
            i++;
        }
        i = peak;
        bool decr = true;
        
        while(decr && i < n - 1){
            if(arr[i + 1] >= arr[i]){
                decr = false;
            }
            i++;
        }
        
        return incr && decr;
            
    }
};