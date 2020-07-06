#include<algorithm>
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        reverse(digits.begin(), digits.end());
        
        int i = 0;
        int n = digits.size();
        int c = 0;
        
        while(i<n){
            
            if(i == 0){
                digits[i] = (digits[i] + 1);
                c = max(0, digits[i] - 9);
                digits[i]%=10;
            }
            else{
                digits[i] = (digits[i] + c);
                c = max(0, digits[i] - 9);
                digits[i]%=10;
            }
            i++;
        }
        if(c){
            digits.push_back(1);
        }
        reverse(digits.begin(), digits.end());
        return digits;
        
        
    }
};