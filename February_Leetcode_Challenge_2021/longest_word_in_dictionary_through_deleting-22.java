class Solution {
    public boolean isSub(String x, String s){
        
        int i = x.length() - 1;
        int j = s.length() - 1;
        
        while(i > -1 && j > -1){
            if(x.charAt(i) == s.charAt(j)){
                i--;
            }
            j--;
        }
        return i == -1;
        
    }
    public String findLongestWord(String s, List<String> d) {
        Collections.sort(d, (String a, String b) -> {
           if(a.length() == b.length()){
               return a.compareTo(b);
           }
           else{
               return b.length() - a.length();    
            }
        });
        
        for(String x: d){
            if(isSub(x, s)){
                return x;
            }
        }
        return "";
    }
}
