class Solution {
    public List<Integer> nums;
    public int[] sums = new int[4];
    public int side;
    
    public boolean dfs(int index){
        if(index == this.nums.size()){
            boolean isSq = true;
            for(int i = 1; i < 4; i++){
                isSq = isSq && (sums[i] == sums[i - 1]);
            }
            return isSq;
        }
        
        int element = this.nums.get(index);
        
        for(int i = 0; i < 4; i++){
            if(this.sums[i] + element <= this.side){
                this.sums[i] += element;
                if(this.dfs(index + 1) == true){
                    return true;
                }
                this.sums[i] -= element;
            }
        }
        return false;
        
    }
    
    public boolean makesquare(int[] nums) {
        int n = nums.length;
        if(n == 0){
            return false;
        }
        
        int allSum = 0;
        for(int s: nums){
            allSum += s;
        }
        
        this.side = allSum / 4;
        if(this.side * 4 != allSum){
            return false;
        }
        
        this.nums = Arrays.stream(nums).boxed().collect(Collectors.toList());
        Collections.sort(this.nums, Collections.reverseOrder());
        return this.dfs(0);
    }
}
