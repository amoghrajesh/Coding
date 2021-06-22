class Solution {
    int ans = 0;
    String big;
    int bign;
    
    public boolean isSubsequence(String w){
        int wn = w.length();
        int i = bign - 1;
        int j = wn - 1;
        
        while(i > -1 && j > -1){
            if(big.charAt(i) == w.charAt(j)){
                j--;
            }
            i--;
        }
        return j == -1;
    }
    
    public int numMatchingSubseq(String s, String[] words) {
        big = s;
        bign = s.length();     
        HashMap<String, Integer> map = new HashMap<>();
        
        for(int i = 0; i < words.length; i++){
            if(map.containsKey(words[i])){
                map.put(words[i], map.get(words[i]) + 1);
            }
            else{
                map.put(words[i], 1);
            }
        }
        
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            String key = entry.getKey();
            int value = entry.getValue();
            
            if(isSubsequence(key) == true){
                ans = ans + value;
            }
            
        }
        return ans;
    }
}
