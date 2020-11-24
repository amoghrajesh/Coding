public class Solution {
    public int calculate(String s) {
        
        s = s.trim().replaceAll(" ","");
        
        String[] nums = s.split("[\\+\\-\\*/]+");
        String[] ops = s.split("[\\d]+");
        Stack<Integer> numsStack = new Stack<Integer>();
        numsStack.push(Integer.parseInt(nums[0]));
        
        for (int i = 1; i < ops.length; i ++) {
            int curr = Integer.parseInt(nums[i]);
            if (ops[i].equals("*")) {
                curr = numsStack.pop() * curr;
            }
            if (ops[i].equals("/")) {
                curr = numsStack.pop() / curr;
            }
            if (ops[i].equals("-")){
                curr = -curr;
            }
            numsStack.push(curr);
        }
        int result = 0;
        while (numsStack.size() > 0) {
            result += numsStack.pop();
        }
        return result;
    }
}