class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stack = new Stack<String>();
        int x, y;
        String result = "";
        int get = 0;
        String choice;
        int value = 0;
        String p = "";
        
        for (int i = 0; i < tokens.length; i++) {
            if (tokens[i] != "+" && tokens[i] != "-"
                && tokens[i] != "*" && tokens[i] != "/") {
                stack.push(tokens[i]);
                continue;
            }
            else {
                choice = tokens[i];
            }
  
            switch (choice) {
            case "+":
                x = Integer.parseInt(stack.pop());
                y = Integer.parseInt(stack.pop());
                value = x + y;
                result = p + value;
                stack.push(result);
                break;
  
            case "-":
                x = Integer.parseInt(stack.pop());
                y = Integer.parseInt(stack.pop());
                value = x - y;
                result = p + value;
                stack.push(result);
                break;
  
            case "*":
                x = Integer.parseInt(stack.pop());
                y = Integer.parseInt(stack.pop());
                value = x * y;
                result = p + value;
                stack.push(result);
                break;
  
            case "/":
                x = Integer.parseInt(stack.pop());
                y = Integer.parseInt(stack.pop());
                value = y / x;
                result = p + value;
                stack.push(result);
                break;
  
            default:
                continue;
            }
        }
        return Integer.parseInt(stack.pop());
    }
}
