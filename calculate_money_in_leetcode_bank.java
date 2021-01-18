class Solution {
    public int totalMoney(int n) {
        if(n == 1){
            return 1;
        }
        int start = 1;
        int prev = 0;
        int sum = 0;
        int i = 0;
        
        while(i < n){
            if(i % 7 == 0){
                prev = prev != 0 ? prev + 1 : 1;
                sum += prev;
                start = prev;
            }
            else{
                start++;
                sum += start;
            }
            i++;
        }
        return sum;
    }
}
