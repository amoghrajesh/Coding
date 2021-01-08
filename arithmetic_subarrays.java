class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        List<Boolean> ans = new ArrayList<>();
        int m = l.length;
        int s, e;
        
        for(int i = 0; i < m; i++){
            s = l[i];
            e = r[i];
            
            int[] temp = Arrays.copyOfRange(nums, s, e + 1);
            Arrays.sort(temp);
            
            if(temp.length > 2){
                int x = temp[1] - temp[0];
                boolean entered = false;
                for(int j = 2; j < temp.length; j++){
                    if(entered == false && temp[j] - temp[j - 1] != x){
                        entered = true;
                        ans.add(false);
                    }
                }
                if(entered == false){
                    ans.add(true);
                }
            }
            else{
                ans.add(true);
            }
        }
        return ans;
    }
}