class Solution {
    public double average(int[] salary) {
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        int sum = 0;
        
        for(int s: salary){
            if(s < min){
                min = s;
            }
            if(s > max){
                max = s;
            }
        }
        
        for(int s: salary){
            sum += s;
        }
        
        sum -= (min + max);
        return sum * 1.0 / (salary.length - 2);
    }
}