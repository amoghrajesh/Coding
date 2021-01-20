class Solution {
    public boolean match(char a, char b){
        if(b == '{' && a == '}'){
            return true;
        }
        else if(b == '[' && a == ']'){
            return true;
        }
        else if(b == '(' && a == ')'){
            return true;
        }
        return false;
    }
    public boolean isValid(String a) {
        Stack<Character> s = new Stack<>();
        for(int i = 0; i < a.length(); i++){
            if(i == 0){
                if(a.charAt(i) == '(' || a.charAt(i) == '[' || a.charAt(i) == '{'){
                    s.push(a.charAt(i));
                }
                else{
                    System.out.println("here");
                    return false;
                }
                continue;
            }
            
            if(a.charAt(i) == '(' || a.charAt(i) == '[' || a.charAt(i) == '{'){
                s.push(a.charAt(i));
            }
            else{
                if(s.empty() == false && match(a.charAt(i), s.peek()) == true){
                    s.pop();
                }
                else{
                    return false;
                }
            }
        }
        return s.empty();
    }
}
