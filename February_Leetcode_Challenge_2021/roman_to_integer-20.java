class Solution {
    public int getInt(char c){
        int x = 0;
        switch(c){
            case 'I': x = 1;
                break;
            case 'X': x = 10;
                break;
            case 'V': x = 5;
                break;
            case 'L': x = 50;
                break;
            case 'C': x = 100;
                break;
            case 'D':x = 500;
                break;
            case 'M': x = 1000;
                break;
        }
        return x;
    }
    public int romanToInt(String s) {
        int i = 0;
        int n = s.length();
        char c;
        int ans = 0;
        
        
        while(i < n){
            c = s.charAt(i);
            if(c == 'I'){
                if(i + 1 < n && (s.charAt(i + 1) == 'V' || s.charAt(i + 1) == 'X')){
                    if(s.charAt(i + 1) == 'V'){
                        ans += 4;
                    }
                    else{
                        ans += 9;
                    }
                    i++;
                }
                else{
                    ans += getInt(c);
                }
                i++;
            }
            else if(c == 'X'){
                if(i + 1 < n && (s.charAt(i + 1) == 'L' || s.charAt(i + 1) == 'C')){
                    if(s.charAt(i + 1) == 'L'){
                        ans += 40;
                    }
                    else{
                        ans += 90;
                    }
                    i++;
                }
                else{
                    ans += getInt(c);
                }
                i++;
            }
            else if(c == 'C'){
                if(i + 1 < n && (s.charAt(i + 1) == 'D' || s.charAt(i + 1) == 'M')){
                    if(s.charAt(i + 1) == 'D'){
                        ans += 400;
                    }
                    else{
                        ans += 900;
                    }
                    i++;
                }
                else{
                    ans += getInt(c);
                }
                i++;
            }
            else{
                ans += getInt(c);
                i++;
            }
        }
        return ans;
    }
}
