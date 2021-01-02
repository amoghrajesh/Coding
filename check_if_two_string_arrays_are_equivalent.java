class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        
        String a = "";
        String b = "";
        
        for(String x: word1){
            a += x;
        }
        for(String x: word2){
            b += x;
        }
        
        int m = a.length();
        int n = b.length();
        
        if(m != n){
            return false;
        }
        
        for(int i = 0; i < m; i++){
            if(a.charAt(i) != b.charAt(i)){
                return false;
            }
        }
        return true; 
    }
}