class MyCircularQueue {
    public int n, f, r;
    public int[] cq;

    public MyCircularQueue(int k) {
        n = k;
        f = r = 0;
        cq = new int[n];
    }
    
    public boolean enQueue(int value) {
        if(isFull()){
            return false;
        }
        cq[(f + 1) % n] = value;
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty()){
            return false;
        }
        r = (r + 1) % n;
        return true;
    }
    
    public int Front() {
        if(isEmpty()){
            return -1;
        }
        return cq[(f - 1) % n];
    }
    
    public int Rear() {
        if(isEmpty()){
            return -1;
        }
        return cq[(r - 1) % n];

    }
    
    public boolean isEmpty() {
        return f == r;
    }
    
    public boolean isFull() {
        return Math.abs(f - r) == n;
    }
}
