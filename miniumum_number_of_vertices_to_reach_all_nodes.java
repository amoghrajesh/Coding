class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        boolean[] canBeReached = new boolean[n];
        
        for(int i = 0; i < edges.size(); i++){
            canBeReached[edges.get(i).get(1)] = true;
        }
        
        List<Integer> ans = new ArrayList<>();
        for(int i = 0; i < n; i++){
            if(canBeReached[i] == false){
                ans.add(i);
            }
        }
        return ans;
    }
}