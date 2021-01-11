class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        HashMap<Character, Integer> map = new HashMap<>();
        
        for(int i = 0; i < allowed.length(); i++){
            if(map.containsKey(allowed.charAt(i)) == false){
                map.put(allowed.charAt(i), 1);
            }
        }
        int ans = 0;
        
        for(String s: words){
            boolean valid = true;
            for(int i = 0; i < s.length(); i++){
                if(map.containsKey(s.charAt(i)) == false){
                    valid = false;
                    break;
                }
            }
            if(valid == true){
                ans++;
            }
        }
        return ans;
    }
}