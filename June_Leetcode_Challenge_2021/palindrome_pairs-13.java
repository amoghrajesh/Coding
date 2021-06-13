class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
         List<List<Integer>> result = new ArrayList<>();

        int len = words.length;
        for(int i =0;i<len; i++){
            for(int j = i+1;j<len;j++){
              
                if(ispalindrome(words[i] + words[j])){
                   result.add(Arrays.asList(i,j));
                }
                if(ispalindrome(words[j] + words[i])){  
                    result.add(Arrays.asList(j,i));
                }

            }

        }
        return result;

    }
    private boolean ispalindrome(String str){
        
        int startIndex = 0;
        int endIndex = str.length()-1;
        
        while(startIndex < endIndex){
            if((str.charAt(startIndex) != str.charAt(endIndex))) return false;
            startIndex++;
            endIndex--;
        }
        
        return true;
        
    }
}
