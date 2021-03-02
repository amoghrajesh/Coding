class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        boolean[] visited = new boolean[n + 1];
        int[] ans = new int[2];
        
        for(int x: nums){
            if(visited[x] == true){
                ans[0] = x;
            }
            else{
                visited[x] = true;
            }
        }
        
        for(int i = 1; i < n + 1; i++){
            if(visited[i] == false){
                ans[1] = i;
            }
        }
        return ans;
    }
}
