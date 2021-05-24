class Solution {
    public String toLowerCase(String s) {
        String ans = "";
        char temp;
        for(int i = 0; i < s.length(); i++){
            temp = s.charAt(i);
            int ascii = (int) temp;
            if(ascii >= 65 && ascii <= 90){
                ascii += 32;
                temp = (char) ascii;
            }
            ans += temp;
        }
        return ans;
    }
}
