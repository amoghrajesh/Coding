class Solution {
    public int minPartitions(String n) {
        int m = Integer.MIN_VALUE;
        int j;
        
        for(int i = 0; i < n.length(); i++){
            j = Character.getNumericValue(n.charAt(i));
            if(j > m){
                m = j;
            }
        }
        return m;
    }
}