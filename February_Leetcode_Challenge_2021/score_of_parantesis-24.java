class Solution {
    public int scoreOfParentheses(String S) {
        Stack<String> s = new Stack<>();
        int i = 0;
        int ans = 0;
        int n = S.length();
        int c = 0;
        
        while(i < n){
            if(S.charAt(i) == '('){
                s.add("(");
            }
            else{
                if(s.peek() == "("){
                    s.pop();
                    s.add("1");
                }
                else{
                    c = 0;
                    while(s.peek() != "("){
                        c += Integer.parseInt(s.peek());
                        s.pop();
                    }
                    
                    s.pop();
                    int innerScore = 2 * c;
                    s.add(String.valueOf(innerScore));
                }
            }
            i++;
        }
        
        while(s.isEmpty() == false){
            ans += Integer.parseInt(s.peek());
            s.pop();
        }
        return ans;
    }
}
