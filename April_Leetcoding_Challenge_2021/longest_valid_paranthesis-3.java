class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        
        int n = s.length();
        char ch;
        int ans = 0;
        
        for(int i = 0; i < n; i++){
            ch = s.charAt(i);
            if(ch == '('){
                stack.push(i);
            }
            else{
                if(stack.isEmpty() == false){
                    stack.pop();
                }
                
                if(stack.isEmpty() == false){
                    ans = Math.max(ans, i - stack.peek());
                }
                else{
                    stack.push(i);
                }
            }
        }
        return ans;
    }
}
