class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        Set<Integer> ans = new HashSet<>();
        for(int i = 1; i <= bound; i = i * x){
            for(int j = 1; j <= bound; j = j * y){
                if(i + j <= bound){
                    ans.add(i + j);
                }
                if(y == 1){
                    break;
                }
            }
            if(x == 1){
                break;
            }
        }
        List<Integer> res = new ArrayList<>();
        for(int v: ans){
            res.add(v);
        }
        return res;
    }
}
