class FreqStack {
    Map<Integer, Integer> freqMap = new HashMap<>();
    Map<Integer, Stack<Integer>> stackMap = new HashMap<>();
    int maxFreq = 0;
    public FreqStack() {

    }
    
    public void push(int x) {
        int f = freqMap.getOrDefault(x, 0);
        freqMap.put(x, ++f);
        
        maxFreq = Math.max(maxFreq, f);
        stackMap.computeIfAbsent(f, z -> new Stack()).push(x); 
        return;
    }
    
    public int pop() {
        int top = stackMap.get(maxFreq).pop();
        int oldFreq = freqMap.get(top);
        freqMap.put(top, oldFreq - 1);
        
        if(stackMap.get(maxFreq).size() == 0){
            maxFreq--;
        }
        return top;
    }
}
