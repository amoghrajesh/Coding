class Solution {
    public boolean sameEncoding(String word, String pattern){
        Map<Character, Character> fwdMap = new HashMap<>();
        Map<Character, Character> bwdMap = new HashMap<>();
        
        if(word.length() != pattern.length()){
            return false;
        }
        int n = word.length();
        for(int i = 0; i < n; i++){
            char w = word.charAt(i);
            char p = pattern.charAt(i);
            
            if(fwdMap.containsKey(w) == false){
                fwdMap.put(w, p);
            }
            if(bwdMap.containsKey(p) == false){
                bwdMap.put(p, w);
            }
            if(fwdMap.get(w) != p || bwdMap.get(p) != w){
                return false;
            }
        }
        return true;
    }
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> ans = new ArrayList<>();
        for(String word: words){
            if(sameEncoding(word, pattern)){
                ans.add(word);
            }
        }
        return ans;
    }
}
