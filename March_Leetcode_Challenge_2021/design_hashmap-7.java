class MyHashMap {
    int[] visited = new int[1000001];
    public MyHashMap() {
        Arrays.fill(visited, -1);
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        this.visited[key] = value;
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        return visited[key];
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        visited[key] = -1;
    }
}
