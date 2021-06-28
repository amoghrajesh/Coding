class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            if(stack.size() == 0){
                stack.push(s.charAt(i));
            }
            else{
                if(s.charAt(i) == stack.peek()){
                    stack.pop();
                }
                else{
                    stack.push(s.charAt(i));
                }
            }
        }
        StringBuffer ans = new StringBuffer();
        while(stack.size() != 0){
            ans.append(stack.pop());
        }
        return ans.reverse().toString();
    }
}
