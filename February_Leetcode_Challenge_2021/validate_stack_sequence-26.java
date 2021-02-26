class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int n = pushed.length;
        Stack<Integer> s = new Stack<>();
        int p = 0;
        
        for(int e: pushed){
            s.push(e);
            while(s.isEmpty() == false && p < n && s.peek() == popped[p]){
                s.pop();
                p++;
            }
        }
        
        return p == n;
    }
}
