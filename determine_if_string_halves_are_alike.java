class Solution {
    public boolean isVowel(char c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
    
    public boolean halvesAreAlike(String s) {
        int n = s.length();
        int part1, part2;
        part1 = part2 = 0;
        
        for(int i = 0; i < n / 2; i++){
            if(isVowel(s.charAt(i))){
                part1++;
            }
        }
        
        for(int i = n / 2; i < n; i++){
            if(isVowel(s.charAt(i))){
                part2++;
            }
        }
        return part1 == part2 ? true : false;
    }
}