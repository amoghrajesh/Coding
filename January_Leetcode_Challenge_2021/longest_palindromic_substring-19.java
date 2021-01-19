class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        boolean dp[][] = new boolean[n][n];
        int m = 1;
        
        for(int i = 0; i < n; i++){
            dp[i][i] = true;
        }
        char a, b;
        int j;
        int start = 0;
        
        for(int i = 0; i < n - 1; i++){
            a = s.charAt(i);
            b = s.charAt(i + 1);
            if(a == b){
                dp[i][i + 1] = true;
                m = 2;
                start = i;
            }
        }
        
        for(int l = 3; l <= n; l++){
            for(int i = 0; i < n - l + 1; i++){
                j = n - l + 1;
                if(dp[i + 1][j - 1] = true && s.charAt(i) == s.charAt(j)){
                    dp[i][j] = true;
                    if(j - i + 1 > m){
                        System.out.println("in" + i + " " + j + " l: " + l);
                        m = j - i + 1;
                        start = i;
                    }
                }
            }
        }
        System.out.println(start + " " + m);
        return s.substring(start, start + m);
    }
}
